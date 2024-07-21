Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def display_rightangled_trinangle(lines):
    for i in range(1, lines +1):
        print('1 ' * i)
        def display_equilareral_tringle(lines):
            for i in range(1, lines + 1):
                print(' ' * (lines - i) + '1 ' * i)
                def main():
                    while True:
                        print("\nMenu:")
                        print("1. Display a right-angled triangle of ones")
                        print("2. Display an equilateral trinagle of ones")
                        print("3. Exit")

                        
choice = int(input("Enter your choice: "))
Enter your choice: if choice ==1 or choice == 2:
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    choice = int(input("Enter your choice: "))
ValueError: invalid literal for int() with base 10: 'if choice ==1 or choice == 2:'
if choice ==1 or choice == 2:
    lines = int(input("Enter the number of lines: "))
    if choice ==1:
...         display_right_angled_trinagle(lines)
...         elif chiuce == 2:
...             
SyntaxError: invalid syntax
>>>  if choice ==2:
...      
SyntaxError: unexpected indent
>>>  if choice == 2:
...      
SyntaxError: unexpected indent
>>> elif choice == 2:
...     
SyntaxError: invalid syntax
>>>  if choice ==1:
...         display_right_angled_trinagle(lines)
...         
SyntaxError: unexpected indent
>>> SyntaxError: unexpected indent
SyntaxError: invalid syntax
>>> 
>>> if choice ==1 or choice == 2:
...    lines = int(input("Enter the number of lines: "))
...    if choice ==1:
...        display_right_angled_trinagle(lines)
... 
...        
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    if choice ==1 or choice == 2:
NameError: name 'choice' is not defined
>>> NameError: name 'choice' is not defined
SyntaxError: invalid syntax
>>> 
>>> if choice == 2:
...     display_equilateral_triangle(lines.")
...                                  
SyntaxError: unterminated string literal (detected at line 2)
>>> SyntaxError: unterminated string literal (detected at line 2)
...                                  
SyntaxError: invalid syntax
>>> 
>>> if choice == 2 :
...        display_equilateral_trinagle(lines)
...                                  if choice == 3
...                                  
SyntaxError: unexpected indent
>>> SyntaxError: unexpected indent
...                                  
SyntaxError: invalid syntax
>>> 
>>> if choice == 3 :
... print("Exiting the program.")
...                                  
SyntaxError: expected an indented block after 'if' statement on line 1
>>> SyntaxError: expected an indented block after 'if' statement on line 1
...                                  
SyntaxError: invalid syntax
>>> 
>>> if choice == 3 :
...                                  print("Exiting the program.")
...                                  while True
                                 
SyntaxError: expected ':'
while True:
    print("Invalid choice, please try again.")
    if __name__"__main__":
        
SyntaxError: invalid syntax
if __name__ == "main__":
    main()
