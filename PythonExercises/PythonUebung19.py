'''
Exercise 19. Multi-Tiered Income Tax Calculation

Practice Problem: Calculate income tax for a given income based on these rules:

First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax
Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. 
It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.
'''

def taxCalculator(income):
    tax_payable = 0
    print("Given Income: ", income)
    
    if income <= 10000:
        #first 10k
        tax_payable = 0
    elif income <= 20000:
        #next 10k
        tax_payable = (income - 10000) * 10 /100
    else:
        #first 10k = 0%
        #second 10k = 10%
        tax_payable = 0 + (10000 * 10 / 100)
        #remaining income = 20%
        tax_payable += (income - 20000) * 20 / 100
    
    print("Total income tax to pay is", tax_payable)
        
taxCalculator(45000)