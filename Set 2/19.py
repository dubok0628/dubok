electricity_units = int(input("Input electricity units: "))

if 0 < electricity_units <= 50:
    electricity_units = electricity_units * 0.5
elif 50 < electricity_units <= 100:
    electricity_units = 50 * 0.5 + (electricity_units - 50) * 0.75
elif 150 < electricity_units <= 250:
    electricity_units = 50 * 0.5 + (electricity_units - 50) * 0.75 + (electricity_units - 150) * 1.20
else:
    electricity_units = 50 * 0.5 + (electricity_units - 50) * 0.75 + (electricity_units - 150) * 1.20 + (electricity_units - 250) * 1.50

final_bill = electricity_units * 1.2

print (f"Your final bill is {final_bill}")