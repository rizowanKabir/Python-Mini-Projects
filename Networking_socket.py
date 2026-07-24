import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.settimeout(2)
    client.connect(("google.com", 80))
    print("Connected Successfully!")

except socket.error as err:
    print("Couldn't connect!")
    print(err)

finally:
    client.close()