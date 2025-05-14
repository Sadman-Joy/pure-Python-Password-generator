import random 
chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+\|?"
length = int(input("Enter length : "))
password = ""

for i in range(length):
    password += random.choice(chars)
print("password is", password)
exit = input("Enter exit or cross if done")
