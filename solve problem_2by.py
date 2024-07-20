Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
... Type "help", "copyright", "credits" or "license" for more information.
... >>> decimal_tobinary(n):
...   File "<stdin>", line 1
...     decimal_tobinary(n):
...                        ^
... SyntaxError: invalid syntax
... >>> return bin(n).replace("0b","")
...   File "<stdin>", line 1
... SyntaxError: 'return' outside function
... >>> def main():
... ... decimal_number = int(input("Enter a decimal number: "))
...   File "<stdin>", line 2
...     decimal_number = int(input("Enter a decimal number: "))
...     ^
... IndentationError: expected an indented block after function definition on line 1
... >>> binary_number = decimal_to_binary(decimal_number)
... Traceback (most recent call last):
...   File "<stdin>", line 1, in <module>
... NameError: name 'decimal_to_binary' is not defined
... >>> print(f"{decimal_number} in binary is {binary_number}")
... Traceback (most recent call last):
...   File "<stdin>", line 1, in <module>
... NameError: name 'decimal_number' is not defined
... >>> if __name__ == "__main__":
... ... main()
...   File "<stdin>", line 2
...     main()
...     ^
... IndentationError: expected an indented block after 'if' statement on line 1
