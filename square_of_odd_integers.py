'''
from a given list of integers, create a new list using comprehension that will compute the square of odd integer elements.

sample calls

[2,4,3] == [9]
[0,0,1,1] == [1,1]

'''

# pseudocode

# make a list
list = [4, 5, 14, 14]

# iterate through the list
squared_list = [element **2 for element in list if element % 2 == 1]

# print the square of the odd element
print(squared_list)