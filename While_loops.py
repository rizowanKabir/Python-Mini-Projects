# print Numbers from 10 to 15

number = 10 
while number <= 15:
    print(number,end=" ")
    number += 1

# Print Cube of numbers from 1 to 5.

number = 1
while number <= 5:
    print(number ** 3,end=" ")
    number += 1

# Print odd numbers 1 to 10.

number = 1
while number <= 10:
    if number % 2 != 0:
        print(number,end=" ")
    number += 1   
 
# print product of number from 1 to 5

product = 1
number = 1
while number <= 5:
    product *= number
    number += 1
print(product)    
