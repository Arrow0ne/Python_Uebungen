'''
Exercise 22. Custom Exponentiation Function

Practice Problem: Write a function called exponent(base, exp) that returns an integer 
value of the base raised to the power of the exponent.

Exercise Purpose: Learn about “Accumulator Patterns.” Although Python has a built-in 
power operator (**), making your own version shows how repeated multiplication works and 
how functions return results to the main program.
'''
def exponent(base, exp):
    sum = 1
    for i in range(exp):
        sum *= base
    print("The sum of ", base, "with the exp ", exp, "= ", sum)
    
exponent(2, 10)