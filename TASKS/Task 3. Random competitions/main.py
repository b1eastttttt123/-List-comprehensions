import random
import math

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(first_team[number], second_team[number]) for number in range(20)]

print("Первая команда:", first_team)
print("Вторая команда:", second_team)
print("Победители тура:", winners)
