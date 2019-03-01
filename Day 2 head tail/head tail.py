import random

condition = "y"
while condition == "y":
    choice = random.randint(0,1)
    if choice == 1:
        print("Head")
    else:
        print("Tail")
    
    input("do you want to toss again(y/n): ")



    