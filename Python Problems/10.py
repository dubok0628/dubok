def approx_term(approx_nterm: int):
    return (4 / (((approx_nterm*2)-2) * ((approx_nterm*2)-1) * (approx_nterm*2)))

terms_list = list()

def usr_input(prompt: str):
    pi_input = int(input(prompt))
    num_elements = pi_input

    for i in range(1, num_elements + 1):
        terms_list.append(i)

    if pi_input == 1:
        return 3
    elif 1 < pi_input <= 15:
        return 3 + 2
    else:
        return 3 + pi_input

my_input = usr_input("Please input the number of approximations for pi: ")

counter = 0
pi_approximate = 3

for i in terms_list:


