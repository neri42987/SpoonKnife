#!/usr/bin/env bash

TAG=$1
TEMP_TAG=$1-stable
RELEASE_NAME=alpha-stable/$TAG

tagcommit=$(git rev-list -n 1 $TAG)
git tag $TEMP_TAG $tagcommit
git push origin $TEMP_TAG

# Create a release
gh release create $TEMP_TAG --title $RELEASE_NAME --notes "Release $RELEASE_NAME" --prerelease

# Check if the release is created
gh release list

# Clean up
git tag -d $TEMP_TAG
git push --delete origin $TEMP_TAG

git fetch --prune --tags

# Find last stable release
gh release list | grep alpha-stable | head -n 1| awk '{print $1}'





