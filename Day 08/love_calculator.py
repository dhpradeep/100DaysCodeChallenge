import os
import time
os.system('cls')

print("Welcome to love calculator.")
love1 = input("Enter prince name: ")
love2 = input("Enter princess name: ")

love1 = sum([ord(c) for c in love1])
love2 = sum([ord(c) for c in love2])

finalLove = int((love1 + love2) % 100)
for i in range(finalLove):
    print(i)
    time.sleep(0.1)
    os.system('cls')

print("Its a {0}% chance to find a love.".format(str(finalLove)))
