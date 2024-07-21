Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def generate_even_squares(numbers):
...     return [x**2 for x in numbers if x % 2 == 0]
... def slice_list(numbers,start, end) :
...     
SyntaxError: invalid syntax
>>> def slice_list(numbers,start, end):
...     return numbers[start:end]
... def main():
...     
SyntaxError: invalid syntax
>>> 
>>> 
>>> def main():
...     numbers = list(map(int, input("Enter the list of integers (comma separated): ").split(',')))
... 
...     
>>> even_squares = geerate_even_squares(numbers)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    even_squares = geerate_even_squares(numbers)
NameError: name 'geerate_even_squares' is not defined
>>> even_squares = generate_even_squares(numbers)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    even_squares = generate_even_squares(numbers)
NameError: name 'generate_even_squares' is not defined
>>> 
>>> 
>>> def generate_even_squares(numbers):
...     return [x**2 for x in numbers if x % 2 == 0]
... def slice_list(numbers,start, end) :
...     
SyntaxError: invalid syntax
>>> 
>>> 
>>> def slice_list(numbers,start, end) :
...    return numbers[start:end]
... 
>>> def main():
...    numbers = list(map(int, input("Enter the list of integers (comma separated): ").split(',')))
...    even_squares =genrate_even_squares(numbers)
...    ptint("Even squares:", even_squares)
...    start = int(input("Enter the end start index for slicing: "))
...    end = int(input("Enter the enf index for slicing: "))
...    sliced_list = slice_list(even_squares,start, end)
...    print("Sliced list:" , sliced_list)
... 
...    
>>> if __name__ == "__main__":
...     main()
