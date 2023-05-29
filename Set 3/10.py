import string
alphabet = list(string.ascii_letters)
shift_amt = int(input("Shift amount: "))

for letter in alphabet:
    index(alphabet) += shift_amt

print(alphabet)
