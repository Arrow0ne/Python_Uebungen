'''
Exercise 27. Finding Common Elements (Intersections)

Practice Problem: Take two lists and find the elements that appear in both. 
Use Sets to perform the operation.

Exercise Purpose: This exercise explores “Mathematical Set Operations.” 
Finding intersections is vital for recommendation engines (e.g., finding “mutual friends” 
or “shared interests”). It demonstrates why using the right data structure (Set) 
is more efficient than nested loops.
'''

def removeDuplicates(listA, listB):
    
    newList = listA + listB
    newList.sort()
    print("Liste 1: ", listA)
    print("Liste 2: ", listB)
    print("Old List: ", newList)
    newSet = set(newList)
    print(newSet)


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

removeDuplicates(list_a, list_b)
