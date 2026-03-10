import random

print('welcome to Password Generater')

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)ABCDEFGHIJKLMNOPQRSTUVWXYZ'


numbers = input('Amount of password to generate: ')
nums = int(numbers)

length = input('How long password would you like to generate: ')
length = int(length)

print('Password generated: ')

for i in range(nums):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)


