# Filtering Lists with Conditional Logic
num_list = [10, 20, 33, 46, 55]
new_list = []
for num in num_list:
    if(num % 5 == 0):
        print(num)