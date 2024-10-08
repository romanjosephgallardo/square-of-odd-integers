# Square of Odd Integers from a list

# Make a list
list = [4, 5, 14, 14]

# Iterate through the list
squared_list = [element **2 for element in list if element % 2 == 1]

# Print the square of the odd element
print(squared_list)