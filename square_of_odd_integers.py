# Square of Odd Integers from a list

# Make a list
list_1 = [2, 4, 3]
list_2 = [0, 0, 1, 1]
list_3 = [4, 5, 14, 14, 1, 4, 18, 9, 1, 14]

# Find the odd elements and square them using list comprehension.
class SquareOfOddIntegers:
    def __init__(self):
        pass

    def computation(self, list):
        squared_list = [element ** 2 for element in list if element % 2 == 1]
        return squared_list

# Print the square of the odd elements that can be found
square_of_odd_elements = SquareOfOddIntegers()
print(square_of_odd_elements.computation(list_1))
print(square_of_odd_elements.computation(list_2))
print(square_of_odd_elements.computation(list_3))