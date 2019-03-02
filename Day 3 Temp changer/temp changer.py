#c to f to k
#k to f to c



def cel2Fer(deg):
    return((deg * (9/5)) + 32)

def fer2kel(fer):
    return((fer-32) * (5/9) + 273.15)

def kel2fer(kel):
    return((kel- 273.15) * (9/5) + 32)

def fer2cel(fer):
    return((fer-32) * (5/9))



while True:
    print("Type 1 for celcius to ferhanite : ")
    print("Type 2 for celcius to kelvin : ")
    print("Type 3 for ferhanite to Kelvin : ")
    print("Type 4 for ferhanite to celcius : ")
    print("Type 5 for kelvin to celcius : ")
    print("Type 6 for kelvin to ferhanite : ")
    

    choice = int(input())

    if choice == 1:
        cel = float(input("insert celcius in float: "))
        print(round(cel2Fer(cel),3))
    elif choice == 2: 
        cel = float(input("insert celcius in float: "))
        print(round(fer2kel(cel2Fer(cel)),3))
    elif choice == 3:
        fer = float(input("insert ferhanite in float: "))
        print(round(fer2kel(fer),3))
    elif choice == 4:
        fer = float(input("insert ferhanite in float: "))
        print(round(fer2cel(fer),3))
    elif choice == 6:
        kel = float(input("insert kelvin in float: "))
        print(round(kel2fer(kel),3))
    elif choice == 5:
        kel = float(input("insert kelvin in float: "))
        print(round(fer2cel(kel2fer(kel)),3))
    else:
        print("invalid number")

    if (input("print E for Exit any other key to continue: ").lower() == "e"):
        exit()
    

