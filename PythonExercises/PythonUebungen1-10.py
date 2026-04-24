# Exercise 1: Arithmetic Product and Conditional Logic
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if(number1 * number2 < 1000):
    print(number1 * number2)
else:
    print(number1 + number2)
'''
solution
def multiplication_or_sum(num1, num2):
     Calculate product
   product = num1 * num2
    
     Check if product is within the threshold
    if product <= 1000:
        return product
    else:
        return num1 + num2

 Testing Case 1
result = multiplication_or_sum(20, 30)
print("The result is", result)
 
Testing Case 2
result = multiplication_or_sum(40, 30)
print("The result is", result)
'''

# Exercise 2:  Cumulative Sum of a Range
print("Printing current and previous number sum in a range(10)")
previous_num = 0

# Loop from 0 to 9
for i in range(10):
    x_sum = previous_num + i
    print(f"Current Number {i} Previous Number {previous_num} Sum: {x_sum}")
    
    # Update previous_num for the next iteration
    previous_num = i
    

#Exercise 3: String Indexing and Even Slicing
word = "pynative"
print("Original String is ", word)

# Method: Using list slicing
# format: [start:stop:step]
even_chars = word[0::2]

print("Printing only even index chars")
for char in even_chars:
    print(char)


#Exercise 4. String Slicing and Substring Removal
def remove_chars(word, n):
    result = word[n::]
    print(result)
    
remove_chars("pynative", 4)
remove_chars("pynative", 2)

#Exercise 5: Variable Swapping (The In-Place Method)
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

#Exercise 6: Calculating Factorial with a 

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial
print(f"Factorial of 5 is {factorial(5)}")

#Exercise 7: List Manipulation: Adding and Removing Elements
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Add a fruit to the end
fruits.append("fig")

# Remove the second fruit (index 1)
fruits.pop(1)

print(fruits)

#Exercise 8: String Reversal
text = "Python"

# Reversing using slicing
reversed_text = text[::-1]

print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

#Exercise 9: Vowel Frequency Counter
sentence = "Learning Python is fun!"
vowels = "aeiou"
count = 0

# Convert to lowercase to handle 'A' and 'a' equally
for char in sentence.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")

#Exercise 10:  Finding Extremes (Min/Max) in a List
nums = [45, 2, 89, 12, 7]

largest = max(nums)
smallest = min(nums)

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")

