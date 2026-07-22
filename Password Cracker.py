import random 

def pass_gen(plen):
    password = ""
    charset = "uryewihsdjkfndsjkfnjfelkrjperewrweroerierowerjer0123456789"
    for i in range(1,plen + 1):
        password = password + random.choice(charset) 
    return password   

plen = int(input("Enter the password len: "))

if plen < 8:
    print("Password must be longer than 8 characters")
    exit()

password = pass_gen(plen) 
print(password)    
