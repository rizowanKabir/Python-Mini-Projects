print("Python Express..!!. It started")  

# Object Oriented Programming

class travel:
    def __init__(self,name,age,contact):
        self.name = name
        self.age = age
        self.contact = contact

    def information(self):
        print(f"Passenger: {self.name} and Age: {self.age}") 

object_1 = travel("Rizowan",25,1773155468)
object_1.information()     

# Age Calculating 

current_year = 2026
birth_year = int(input("Enter your birth_year please: "))

age = current_year - birth_year
print(f"Your age is: {age} years")

# Check this is even or odd numbers

number = int(input("Enter the number: "))

if number % 2 == 0:
    print(f"{number} is even number.")
else:
    print(f"{number} is Odd number.")    

# print multiplication 1 to 10

number = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

# Passengers list using loop

passengers = []

for i in range(3):
    name = input(f"Enter passenger {i + 1} name: ")
    passengers.append(name)

print("\nPassenger List:")

for name in passengers:
    print(name) 

# Mini bank system in oop

class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, taka):
        self.balance += taka

    def check(self):
        print(f"Current Balance: {self.balance} Taka")


account = Account()

account.deposit(500)

account.check()

# Using Pandas

import pandas as pd
data = {
"product": ["Shirt", "Pant", "Shirt", "Cap",
"Pant", "Shirt"],
"price": [500, 800, 500, 200, 800, 500],
"area": ["Dhaka", "Dhaka", "Ctg", "Dhaka", "Ctg",
"Ctg"],
}
df = pd.DataFrame(data)
print(df) 

# Using matplotlib & seaborn

import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sell = [50000, 65000, 48000, 80000, 72000, 90000]
plt.plot(months, sell, marker="o") # line chart
plt.title("6 months sell")
plt.xlabel("month")
plt.ylabel("selling(Money)")
plt.show() 

# Using pygame library

import pygame

# Initialize Pygame
pygame.init()

# Create Window
porda = pygame.display.set_mode((400, 300))
pygame.display.set_caption("চালাও!")

# Clock
clock = pygame.time.Clock()

# Initial Position
x, y = 200, 150
goti = 5

cholche = True

while cholche:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cholche = False

    # Check which key is pressed
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        x -= goti

    if key[pygame.K_RIGHT]:
        x += goti

    if key[pygame.K_UP]:
        y -= goti

    if key[pygame.K_DOWN]:
        y += goti

    # Keep the circle inside the window
    x = max(20, min(380, x))
    y = max(20, min(280, y))

    # Fill background
    porda.fill((13, 17, 23))

    # Draw Circle
    pygame.draw.circle(porda, (45, 212, 191), (x, y), 20)

    # Update Screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)

pygame.quit()




    
