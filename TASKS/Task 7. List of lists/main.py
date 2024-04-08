nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [num2 for num1 in nice_list for num2 in [number for num in num1 for number in num]]

print(result)


