'''
Exercise 16. Numerical Palindrome Check

Practice Problem: Write a program to check if a given number is a 
palindrome (reads the same forwards and backwards).

Exercise Purpose: This exercise introduces the idea of “Reversing Logic.” 
Reversing a string is simple, but reversing an integer takes some math, 
like using division and modulo, or changing its type. This shows how data types can work differently.
'''

def checkPalindrome(number):
    print("Original Number", number)
    StringNumber = str(number)
    ReversedNumber = StringNumber[::-1]
    if(StringNumber == ReversedNumber):
        print("Yes, ", StringNumber, " is a Palindrome")
    else:
        print("No, ", StringNumber, " is not a Palindrome")
        
checkPalindrome(121)
checkPalindrome(125)