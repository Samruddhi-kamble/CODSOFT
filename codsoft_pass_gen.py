import random
import string
length=int(input("Enter password length:"))
characters=string.digits+string.ascii_letters+string.punctuation

password=""
for i in range(length):
    password+=random.choice(characters)
print("Password is generated:",password)