original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

for x in original_prices:

    if x < 0:
        original_prices[original_prices.index(x)] = 0

print("Result:", original_prices)
