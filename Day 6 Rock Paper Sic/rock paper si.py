import random
def rand():
    return(random.choice(["rock","paper", "scissor"]))

while True:
    print("This is best of 3 game: ")
    for i in range(3):
        input("Press any key to suffle :")
        p1 = rand()
        p2 = rand()
        print(" player 1 : "+p1 + "\n player 2 : " + p2)
        
        if p1 == "rock" and p2 == "rock":
            print("draw")
        elif p1 == "rock" and p2 == "paper":
            print("player 2 wins")
        elif p1 == "rock" and p2 == "scissor":
            print("player 1 wins")
        elif p2 == "paper" and p1 == "scissor":
            print("player 2 wins")
        elif p2 == "rock" and p1 == "scissor":
            print("player 1 wins")
        elif p2 == "scissor" and p1 == "scissor":
            print("draw")
        elif p1 == "paper" and p2 == "paper":
            print("draw")
        elif p1 == "paper" and p2 == "rock":
            print("player 1 wins")
        elif p1 == "paper" and p2 == "scissor":
            print("player 2 wins")

    if input("Type E if you want to exit").lower() == "e":
        exit()