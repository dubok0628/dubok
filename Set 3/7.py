age_list = list()
price_list = list()
price = 0

while 0 not in age_list:
    usr_input = float(input("Please input the age of the guest (0 if done): "))
    age_list.append(usr_input)

    for element in age_list:
        if element < 3:
            price = 0
        elif 3 <= element <= 12:
            price = 14
        elif element > 64:
            price = 18
        else:
            price = 23

    price_list.append(price)

for element in price_list:
    price += element

print(f"The total price is ${price}")
