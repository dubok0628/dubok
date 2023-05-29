weight = float(input("What is your weight?: "))
height = float(input("What is your height in meters?: "))
BMI = weight / (height**2)

print(f"Your BMI is currently {BMI:.2f}")