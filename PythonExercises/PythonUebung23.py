'''
Exercise 23. Check Palindrome Number

Practice Problem: Write a program to check if a given number is a palindrome. 
A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

Exercise Purpose: This exercise teaches “Algorithmic Reversal.” 
While strings are easy to reverse in Python, reversing a number mathematically 
using the modulo (%) and floor division (//) operators deepens understanding of 
how integers are stored in memory and how to manipulate digits individually.
'''
def isPalindrome(oldNumber):
    originalNumber = oldNumber
    reversedNumber = 0
    while oldNumber > 0:
        digit = oldNumber % 10
        reversedNumber = reversedNumber * 10 + digit
        oldNumber = oldNumber // 10
    
    if originalNumber == reversedNumber:
        print(f"Original number {originalNumber}")
        print("Yes. Given number is palindrome number")
    else:
        print(f"Original number {originalNumber}")
        print("No. Given number is not palindrome number")
        
isPalindrome(121)
isPalindrome(142)