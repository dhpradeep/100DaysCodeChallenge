import random
import time
import os

def suffleHeadTail():
    num = [1,2]
    timer = 0
    while timer != 10:
        os.system('cls')
        print(random.choice(num))
        time.sleep(0.05)
        timer = timer + 0.5
    os.system('cls')


def suffleCoin(predict = ''):
    suffleHeadTail()
    result = ""
    coins = ['Head', 'Tail']
    coin = random.choice(coins)
    if predict == '':
        result =  "Its " + coin
    else:
        predict = 'Head' if predict == 'h' else 'Tail'
        if predict == coin:
            result =  "Wow! your prediction is correct. Its " + coin
        else:
            result =  "Ohhh! Its " + coin
    return result

while 1:
    predict = input("You can predict for coin(H/T)\n(press `enter` to continue) :")
    
    if not (predict.lower() == 'h' or predict.lower() == 't'):
        print(suffleCoin())
    else:
        print(suffleCoin(predict.lower()))
    tryAgain = input("Wanna try again(Y): ")
    if  tryAgain.lower() != 'y':
        break

print("Thank you for playing this game.")
time.sleep(1)