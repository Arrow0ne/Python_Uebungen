'''
Exercise 15. Nested Loops for Pattern Generation

Practice Problem: Print the following pattern where each row 
contains a number repeated a specific number of times based on its value.

Exercise Purpose: Pattern printing is a classic way to learn “Nested Loops.” 
You coordinate an outer loop for rows and an inner loop 
for columns or repetitions. This improves spatial logic and control over output formatting.
'''
for i in range(1, 6):
    for t in range(i):
        print(i, end = " ")
    print("\n")