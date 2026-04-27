#Exercise 18. Integer Digit Extraction and Reversal

def extractDigits(number):
    print("Given number: ", number)
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end = " ")
        
extractDigits(7536)