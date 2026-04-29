'''
Exercise 28. Odd/Even List Splitter

Practice Problem: Start with a list of 10 numbers. 
Iterate through them and sort them into two separate lists: 
one for even numbers and one for odd numbers.
'''

def oddEvenSplitter(listT):
    evenA = []
    oddB = []
    
    for i in listT:
        if(i % 2 == 0):
            evenA.append(i)
        else:
            oddB.append(i)
    
    evenA.sort()
    oddB.sort()
    
    print(f"Even: {evenA} ")
    print(f"Odd: {oddB} ")
    
    
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

oddEvenSplitter(numbers)