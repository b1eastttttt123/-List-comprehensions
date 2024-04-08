
number_user = int(input("Введите длину списка: "))

user_list = [1 if num % 2 == 0 else num % 5 for num in range(number_user)]

print(user_list
