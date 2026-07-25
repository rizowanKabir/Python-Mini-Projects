"""
Actual Credentials
Email: sohagrizowan@gmail.com
password: kabir@123 
"""

email = input("Enter the email: ")
password = input("Enter the password: ")

actual_email = "sohagrizowan@gmail.com"
actual_password = "kabir@123"

if email == actual_email and password == actual_password:
    print("Login successful.!")
if email == actual_email and password != actual_password:  
    print("Please try again.!")
    password = input("Enter the pass word again: ")
    if password == actual_password:
        print("Success!!")
    else:
        print("Wrong.!!")      
else:
    print("Incorrect credentials..!!")    