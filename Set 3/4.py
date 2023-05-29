import math

prices_list = list()
prices = 0

while 0 not in  prices_list:
    usr_input = float(input("Please enter the price of your item: "))
    prices_list.append(usr_input)

for element in prices_list:
    prices += element

print("The sum of prices: ", (round(prices, 2)))
pennies = prices%1

nickels = pennies%0.05
if nickels < 0.025:
    prices = math.floor(prices * 20) / 20
else:
    prices = math.ceil(prices * 20) / 20

print("The total amount to be paid in cash: ", prices)
