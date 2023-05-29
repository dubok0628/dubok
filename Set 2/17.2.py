from math import sqrt

quadratic_term = int(input("Please enter a quadratic term for the polynomial: "))
linear_term = int(input("Please enter a linear term for the polynomial: "))
constant_term = int(input("Please enter a constant term for the polynomial: "))

pos_root = (-linear_term + sqrt(linear_term**2 - 4*quadratic_term*constant_term)) // 2*quadratic_term
neg_root = (-linear_term - sqrt(linear_term**2 - 4*quadratic_term*constant_term)) // 2*quadratic_term

print(f"The first root is the positive root: {pos_root}")
print(f"The second root is the negative root: {neg_root}")