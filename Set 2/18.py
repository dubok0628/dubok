salary = int(input("Please input the salary of your employee: "))

if salary <= 10000:
    HRA = int(salary*0.2)
    DA = int(salary*0.8)
elif salary <= 20000:
    HRA = int(salary*0.25)
    DA = int(salary*0.9)
else:
    HRA = int(salary*0.3)
    DA = int(salary*0.95)

print ("HRA:", HRA)
print ("DA:", DA)
print ("Gross salary is: ", salary + HRA + DA)