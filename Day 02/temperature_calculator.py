import time
import os

def keltocels(val):
    return val - 273
def celstofahr(val):
    return (val * (9/5)) + 32
def fahrtocels(val):
    # (°F − 32) x 5/9
    return ((val - 32) * 5/9)
def celstokel(val):
    return val + 273

if __name__ == '__main__':
    while True:
        print("1. Celc2Fahr") # 0c = 0fahr 273kel
        print("2. Celc2Kel") # 100c = 180fahr 373kel
        print("3. Fahr2Cels")
        print("4. Fahr2kel")
        print("5. Kel2Fahr")
        print("6. Kel2Celc")

        choose = input("Choose (1-6):")
        if not ((isinstance(choose, int) or isinstance(choose, float)) or (int(choose) <= 6 and int(choose) >= 1)):
            print("Choose between 1-6.")
        else:
            val = int(input("Choose value:"))
            if choose == '1':
                print(celstofahr(val))
            elif choose == '2':
                print(celstokel(val))
            elif choose == '3':
                print(fahrtocels(val))
            elif choose == '4':
                print(celstokel(fahrtocels(val)))
            elif choose == '5':
                print(celstofahr(keltocels(val)))
            elif choose == '6':
                print(keltocels(val))
            else:
                    print("Error input.")
        again = input("Wanna try again (Y): ")
        if again.lower() != 'y':
            break
        os.system('cls')

time.sleep(2)