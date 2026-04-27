'''
Exercise 12. List Comparison and Boolean Logic (First and Last digit the same?)

Practice Problem: Write a function to return True if the first and last number 
of a given list is the same. If the numbers are different, return False. 

Exercise Purpose: This exercise introduces “Collection Indexing” and 
“Boolean Flags.” Comparing data structure boundaries is common in pattern matching 
and data integrity checks.
'''

numbers_x = [10 ,20 ,30 ,40 ,10]
numbers_y = [75, 65, 35 ,75, 30]

print("numbers_x? ", numbers_x[0] == numbers_x[-1])
print("numbers_y? ", numbers_y[0] == numbers_y[-1])