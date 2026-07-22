import random  

def save(address):
    with open("mac_address.txt","a") as file:
        file.write(address + "\n")
    
def mac_gen():
    mac_address = ""
    count = 0
    charset = "1234567890abcdef"
    for i in range(1, 12 + 1):
        count = count + 1
        mac_address = mac_address + random.choice(charset)

        if count == 2:
            mac_address = mac_address + "-"
            count = 0
    return mac_address 

for i in range(1, 20 + 1):
    address = mac_gen()
    print(address[:-1].upper())  
 
    save(address )       
