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
  
# Reverse each word in a sentence

sentence = input("Enter the sentence: ")
words = sentence.split()

for word in words:
    i = len(word) - 1
    while i >= 0:
        print(word[i],end=" ")
        i -= 1
    print(end=" ")    

# Count consonant of a string

word = input("Enter the word to check: ")
vowels = "aeiou"
count = 0
index = 0

while index < len(word):
    if word[index].lower() not in vowels and word[index].isalpha():
        count += 1
    index += 1

print(f"Number of consonant is: {count}")       
 
# Print the first 5 Multiples of 3

multiple = 3
count = 1

while count <= 5:
    print(multiple, end=" ")
    multiple += 3
    count += 1
