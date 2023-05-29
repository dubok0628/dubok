angle_1 = float(input("Please input the first angle of your triangle "))
angle_2 = float(input("Please input the second angle of your triangle "))
angle_3 = float(input("Please input the third angle of your triangle "))

if angle_1 + angle_2 + angle_3 == 180:
    print("These 3 angles create a valid triangle")
else:
    print("These 3 angles do not create a valid triangle")