import random

start_range = int(input("Enter the initial range: "))
end_range = int(input("Enter the end range: "))

total_range = [random.randint(start_range, end_range) for _ in range(start_range, end_range)]

print(total_range)
