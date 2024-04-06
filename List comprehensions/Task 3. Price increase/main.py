def task(n):
    score_one = 0

    for num in cost_products:
        score_one += num
        percent = score_one * n / 100
        summ = percent + score_one
    print(round(summ, 2), end=" ")

cost_products = [float(input(f"The price for {i} product: ")) for i in range(1, 5 + 1)]

one_year_percent = float(input("Promotion for the first year: "))
two_year_percent = float(input("Promotion for the second year: "))

print("The sum of prices for each year:", end=" ")

task(0)
task(one_year_percent)
task(two_year_percent)

