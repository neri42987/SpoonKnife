#!/usr/bin/env bash

TAG=$1
TEMP_TAG=$1-stable
RELEASE_NAMME_PREFIX="alpha-stable/"
RELEASE_NAME=$RELEASE_NAMME_PREFIX$TAG

# Create a temporary tag to create a release
tagcommit=$(git rev-list -n 1 $TAG)
git tag $TEMP_TAG $tagcommit
git push origin $TEMP_TAG

# Create the GH release
gh release create $TEMP_TAG --title $RELEASE_NAME --notes "Release $RELEASE_NAME" --prerelease

# Check if the release is created
gh release list

# Clean up the temporary tag
git tag -d $TEMP_TAG
git push --delete origin $TEMP_TAG
git fetch --prune --tags

# Find last stable release
stableReleaseName=$(gh release list | grep alpha-stable | head -n 1| awk '{print $1}')
stableReleaseVersion=${stableReleaseName/"$RELEASE_NAMME_PREFIX"/}
echo "Last stable release: $stableReleaseName version=$stableReleaseVersion"
stablecommit=$(git rev-list -n 1 $stableReleaseVersion)
echo "alpha=$tagcommit stable=$stablecommit"





