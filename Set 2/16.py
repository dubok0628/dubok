a = float(input("Input the length of the 1st side of your triangle"))
b = float(input("Input the length of the 2nd side of your triangle"))
c = float(input("Input the length of the 3rd side of your triangle"))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Your triangle is equilateral")
    elif a == b or a == c or b == c:
        print("Your triangle is isosceles")
    else:
        print("Your triangle is scalene")