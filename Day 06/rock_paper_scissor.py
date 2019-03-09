import random
import os

def rockPaperScissor(val1, val2, player = 'computer'):
    if player == 'computer':
        player1 = 'player'
        player2 = 'computer'
    else:
        player1 = 'player1'
        player2 = 'player2'

    if val1 == val2:
        return("Tie!")
    elif val1 == "rock":
        if val2 == "paper":
            return player2 + " win! " + val2 + " covers " + val1 + "."
        else:
            return player1 + " win! " + val1 + " smashes " + val2 + "."
    elif val1 == "paper":
        if val2 == "scissors":
            return player2 + " win! " + val2 + " cut " + val1 + "."
        else:
            return player1 + " win! " + val1 + " covers " + val2 + "."
    elif val1 == "scissors":
        if val2 == "rock":
            return player2 + " win! " +  val2 + " smashes " + val1 + "."
        else:
            return player1 + " win! " + val1 + " cut " + val2 + "."
    else:
        return "That's not a valid play. Check your spelling!"

def PlayerVsComputer(player):
    if player in ['1','2','3']:
        player = 'scissors' if (player != '2' and player != '1') else 'rock' if player != '1' else 'paper'
        computer = random.choice(['rock','paper','scissors'])
        return rockPaperScissor(player,computer)
    else:
        return "Input Error"

def PlayerVsPlayer(player1,player2):
    if (player1 in ['1','2','3']) and (player2 in ['1','2','3']):
        player1 = 'scissors' if (player1 != '2' and player1 != '1') else 'rock' if player1 != '1' else 'paper'
        player2 = 'scissors' if (player2 != '2' and player2 != '1') else 'rock' if player2 != '1' else 'paper'
        return rockPaperScissor(player1,player2, 'player')
    else:
        return "Input Error"

while True:
    os.system('cls')
    choice = input("1. Player Vs. Computer \n2. Player Vs. Player (1/2): ")
    if choice == '1':
        player = input("1. Paper / 2. Rock / 3. scissor (1,2,3): ")
        print(PlayerVsComputer(player))
    elif choice == '2':
        player1 = input("Player1: 1. Paper / 2. Rock / 3. scissor (1,2,3): ")
        player2 = input("Player2: 1. Paper / 2. Rock / 3. scissor (1,2,3): ")
        print(PlayerVsPlayer(player1,player2))
    else:
        print("Input error.")
    tryagain = input("Try again ? (y/n): ")
    if tryagain.lower() != 'y':
        break
