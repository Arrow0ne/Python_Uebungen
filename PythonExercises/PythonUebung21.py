'''
Exercise 21. Downward Half-Pyramid Pattern

Practice Problem: Print a downward half-pyramid pattern using stars (*).

Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries 
in reverse is important for algorithms that process data from end to beginning.
'''

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()