character = str(input("Input your character: "))

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

if character in vowels:
    print (f"{character} is a vowel")
elif character in consonants:
    print (f"{character} is a consonant")
else:
    print ("Invalid character")