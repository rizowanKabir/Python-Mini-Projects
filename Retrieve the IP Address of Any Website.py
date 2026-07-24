import socket 

try:
    ip = socket.gethostbyname("blood-finder-web-app.onrender.com")
    print(ip)
except socket.gaierror:
    print("Please provide a valid Domain name..!!")     