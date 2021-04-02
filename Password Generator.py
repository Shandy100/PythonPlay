import random
print("Password Generator")
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()<>?,./;:[]{}012356789'
num=int(input("Number of password:\n"))

len=int(input("Length of password:\n"))

for pwd in range(num):
    password=""
    for c in range(len):
        password+=random.choice(chars)
    print(password)
