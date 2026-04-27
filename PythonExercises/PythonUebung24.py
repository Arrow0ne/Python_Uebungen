'''
Exercise 24. Generate Fibonacci Series

Practice Problem: Write a program to print the first 15 terms of the Fibonacci series. 
The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

Exercise Purpose: The Fibonacci sequence is a classic way to learn about state management in loops. 
You keep track of two changing variables at once to find the next number, 
which helps you see how data moves through each step.
'''
num1 = 0
num2 = 1
print(num1, end = " ")
print(num2, end = " ")
for i in range(13):
    print(num1 + num2, end = " ")
    temp = num1
    num1 = num2
    num2 = temp + num2