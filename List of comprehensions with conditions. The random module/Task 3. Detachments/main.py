import random

squad1 = [random.randint(50, 80) for _ in range(10)]
squad2 = [random.randint(30, 60) for _ in range(10)]
squad3 = ["Died" if squad1[damage] + squad2[damage] > 100 else "Survived" for damage in range(10)]

print("Damage of the first squad:", squad1)
print("Damage of the second squad:", squad2)
print("Status of the third squad:", squad3)
