import os
import random
import time

def drawHangman(step):
    print("\n")
    if step == 6:
        print("   /----.")
        print("   |   (_)")
        print("   |    | ")
        print("   |   /|\\")
        print("   |   /|\\")
        print("   |       ")
        print("___|____")
    elif step == 5:
        print("   /----.")
        print("   |   (_)")
        print("   |    | ")
        print("   |   /|\\")
        print("   |       ")
        print("   |       ")
        print("___|____")
    elif step == 4:
        print("   /----.")
        print("   |   (_)")
        print("   |      ")
        print("   |       ")
        print("   |       ")
        print("   |       ")
        print("___|____")
    elif step == 3:
        print("          ")
        print("   |      ")
        print("   |      ")
        print("   |       ")
        print("   |       ")
        print("   |       ")
        print("___|____")
    elif step == 2:
        print("          ")
        print("          ")
        print("          ")
        print("           ")
        print("           ")
        print("           ")
        print("___|____")
    elif step == 1:
        print("\n\n\n\n\n\n")

def help():
    while True:
        os.system('cls')
        print("1. You have 6 life points.")
        print("2. Goto level menu to choose game level.")
        print("3. If you type string in guessing, it only take first word.")
        print("\tFor eg: enter your guess: 'ast' than it only take 'a'")
        val = input("press any key to exit.")
        if val:
            break
    os.system('cls')
    menu()

def questions(value):
    question = []
    if value == 'easy':
        question = ['apple', 'banana', 'mango', 'elephant']
    elif value == 'medium':
        question = ['between', 'again', 'everyone', 'dealer']
    elif value == 'hard':
        question = ['guess', 'congratulation', 'astrology', 'physics']
    return random.choice(question)

def end(val,question,level):
    # os.system('cls')
    if val == 'loose':
        print("Game over. Sorry you loose.")
        print("Correct answer is: '" + question + "'")
    elif val == 'win':
        print("\nGame over. Congratulation you win!!")
    d = input("Try again(y/n): ")
    if d.lower() != 'y':
        exit(1)
    else:
        main(level)

def menu():
    print("1. Play Game")
    print("2. Choose Level(default 'medium')")
    print("3. Help (1/2/3)")
    val = input()
    level = 'medium'
    if val == '1':
        main(level)
    elif val == '2':
        os.system('cls')
        level = input("1. Easy \n2. Medium \n3. Hard (1/2/3):")
        if level == '1':
            level = 'easy'
        elif level == '2':
            level = 'medium'
        elif level == '3':
            level = 'hard'
        main(level)
    elif val == '3':
        help()    

def main(level):
    val = 1
    j = 0
    question = questions(level)
    alreadyGivenWord = []
    corrctWord = []
    while True:
        count = 0
        if val >= 6:
            os.system('cls')
            drawHangman(6)
            print('\n')
            time.sleep(1)
            end('loose',question,level)
        os.system('cls')
        print('\n')
        for i in question:
            if i in corrctWord:
                count = count + 1
                print(i, end=' ')
            else:
                print(' ', end = ' ')
        if count == len(question):
            end('win',question,level)
            
        print("\n")
        print(''.join('_ ' for i in question))
        drawHangman(val)
        print("Mistakes: " + ','.join(i for i in alreadyGivenWord))
        print("Correct words: " + ','.join(i for i in corrctWord))
        print("Remaining guess: " + str(6-val))
        data = input("Enter your guess: ")[0]
        # data = data[0]
        if data in question:
            if data not in corrctWord:
                corrctWord.insert(j,data)
        else:
            if data not in alreadyGivenWord:
                alreadyGivenWord.insert(val-1,data)
                val = val + 1


if __name__ == '__main__':
    menu()
