a = float(input("Input the length of the 1st side of your triangle"))
b = float(input("Input the length of the 2nd side of your triangle"))
c = float(input("Input the length of the 3rd side of your triangle"))

if a + b > c and a + c > b and b + c > a:
    print(f"Your triangle is a valid triangle with sides {a}, {b}, and {c}")
else:
    print(f"Sides {a}, {b}, and {c} do not form a valid triangle")