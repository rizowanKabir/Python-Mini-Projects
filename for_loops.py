# for loop print 1 - 5

for i in range(1,6):
    print(i,end=" ") 

# Print Square of number from 1 to 5

for i in range(1,6):
    print(i ** 2,end=" ")    

# Print Even number from 1 to 10 

for i in range(1,11):
    if i % 2 == 0:
        print(i,end=" ")

#Calculate Sum of number 1 to 10

total = 0
for i in range(1,11):
    total += i
print(f"Total number of sum: {total}")

# Reverse a word using loop

words = "Python"
reverse = ""

for char in words:
    reverse = char + reverse

print(reverse)

# Count Vowel a string

vowels = "aeiou"
word = input("Enter the words: ")
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"total vowels in {word} is {count}")     
    
# print fibonacci sequence up to 10 terms

n = 10

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b 

# Factorial of a number 

n = int(input("Enter the number: "))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(f"Factorial of {n} is {factorial}")  

# Check if a number is prime 

num = int(input("Enter the number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")  
 
# string counting

word = "programming"
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)              



