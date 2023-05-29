character = str(input("Please input your character: "))

for c in character:
    if c.islower():
        print (f"{character} is lowercase")
    elif c.isupper():
        print (f"{character} is uppercase")
    else:
        print (f"{character} is neither lowercase nor uppercase ")