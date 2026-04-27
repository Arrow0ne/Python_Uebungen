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