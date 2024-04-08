import random

original_prices = [random.randint(-100, 100) for _ in range(5)]

new_prices = original_prices

score = 0
print("Market price Full:", original_prices)

for i in range(len(original_prices)):

    if new_prices[i] < 0:
        score -= new_prices[i]
        new_prices[i] = 0
        
print("Market price Update:", original_prices)
print("We've lost:",  score)
