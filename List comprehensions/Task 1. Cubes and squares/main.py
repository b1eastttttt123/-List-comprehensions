# Creating an input
left_border = int(input("The left border: "))
right_border = int(input("The right border: "))

# Creating lists
cube_range = [left_border ** 3 for left_border in range(left_border, right_border + 1)]
squares_range = [left_border ** 2 for left_border in range(left_border, right_border + 1)]

# Output
print("A list of cubes of numbers in the range from", left_border, "to", right_border, ":", cube_range)
print("A list of squares of numbers in the range from", left_border, "to", right_border, ":", squares_range)
