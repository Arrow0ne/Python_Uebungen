'''
Exercise 18. Integer Digit Extraction and Reversal

Practice Problem: Write a program to extract each digit from an integer in the reverse order.

Exercise Purpose: This exercise explores “Mathematical Parsing.” 
Instead of converting a number to a string, use the modulo operator (%) and 
floor division (//) to isolate digits. This is common in low-level programming and 
algorithm challenges where type conversion is restricted.
'''

def extractDigits(number):
    print("Given number: ", number)
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end = " ")
        
extractDigits(7536)