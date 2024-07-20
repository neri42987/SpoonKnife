import re
def validate_usernmae(username):
    if 1 <= len(username) <= 50:
        return "Username is valid."
    else:
        return "Username is invalid."
    def validate_password(password):
        if len(password) >=8 and re.serch(r'\W' , password)and re.search(r'\d' , password) and re.search(r'[A-Z]' , password) and re.search(r'[a-z]', password):
            return "Password is valid."
        else:
            return "Password is invalid."
         def validate_email(email):
            email_regex =r'^[a-zA-Z0-9._%+-]+@{a-zA-Z0-9.0]+\.[A-Za-Z]{2,}$'
            if re.match(email_regex, email):
                return "Email is valid."
            else:
                return "Email is invalid."
            def main():
                username = input("Enter username: ")
                password = input("Enter password: ")
                emai = input("Enter email: ")

                 print(validate_username(username))
                 print(validate_password(password))
                 print(validate_email(email))
                 if __name__== "__main__":
                     main()
                     

