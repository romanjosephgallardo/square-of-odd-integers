# Square of Odd Integers from a list

# Make a list
list = [4, 5, 14, 14]

# Find the odd elements and square them using list comprehension.
squared_list = [element ** 2 for element in list if element % 2 == 1]

# Print the square of the odd elements that can be found
print(squared_list)