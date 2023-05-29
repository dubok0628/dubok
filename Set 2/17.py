from math import sqrt
a = int(input("Please input the integer of the quadratic term of your quadratic equation: "))
b = int(input("Please input the integer of the linear term of your quadratic equation: "))
c = int(input("Please input the integer of the constant term of your quadratic equation: "))


x1 = (-b + sqrt(b**2 - 4*a*c)) // 2 * a
x2 = (-b - sqrt(b**2 - 4*a*c)) // 2 * a

print(f"The roots of the quadratic equation are: {x1} and {x2}")