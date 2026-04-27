'''
Exercise 13. Filtering Lists with Conditional Logic

Practice Problem: Iterate through a given list of numbers and print 
only those numbers which are divisible by 5. 

Exercise Purpose: This exercise teaches the use of the modulo operator (%) 
and loop filtering. In data processing, you often need to sift through large datasets 
to extract subsets that meet mathematical criteria.
'''

num_list = [10, 20, 33, 46, 55]
new_list = []
for num in num_list:
    if(num % 5 == 0):
        print(num)