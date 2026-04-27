#Exercise 19. Multi-Tiered Income Tax Calculation

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