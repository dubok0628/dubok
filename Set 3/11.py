palindrome = str(input("Enter your word: "))

if palindrome == palindrome[::-1]:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")

