def discount_calculator(input_list: list[float,...], discount_rate: float):
    discount_amount_list = list()
    for index, price in enumerate(input_list):
        input_list[index] = price * (1 - discount_rate/100)
        discount_amount = price * discount_rate/100
        discount_amount_list.append(discount_amount)
    print(discount_amount_list)
    return input_list

print(discount_calculator([4.95, 9.95, 14.95, 19.95, 24.95], 60.0))

