import random

def generatePassword(CapitalLettersLength,NumberLength,SmallLettersLength,SpeicalLettersLength):
    SmallLetters = 'abcdefghijklmnopqrstuvwxyz'
    CapitalLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SpeicalLetters = '!@#$%^&*(){}"|?>:<>,./;\'\\[]'
    Numbers = '1234567890'

    randomCapitalLetter = [random.choice(CapitalLetters) for _ in range(CapitalLettersLength)]  
    randomSmallLetter = [random.choice(SmallLetters) for _ in range(SmallLettersLength)]    
    randomNumbers = [random.choice(Numbers) for _ in range(NumberLength)]
    randomSpecialLetter = [random.choice(SpeicalLetters) for _ in range(SpeicalLettersLength)]

    password = randomCapitalLetter + randomSmallLetter + randomNumbers + randomSpecialLetter
    random.shuffle(password)
    password = ''.join(i for i in password)
    
    return password

def generate(level=None,length=None):

    Passwordlevel = level
    PasswordLength = int(length)

    if Passwordlevel == 'easy':
        # 20% = capitalLetter , 20% = number , remaining = smallLetter
        CapitalLettersLength  = round(PasswordLength * 0.2)
        NumberLength = round(PasswordLength * 0.2)
        SmallLettersLength  = round(PasswordLength - CapitalLettersLength - NumberLength)
        SpeicalLettersLength = 0

    if Passwordlevel == 'medium':
        # 20% = capitalLetter, 20% = number, 20% = specialLetter , remaining = smallLetter
        CapitalLettersLength  = round(PasswordLength * 0.2)
        NumberLength = round(PasswordLength * 0.2)
        SpeicalLettersLength = round(PasswordLength * 0.2)
        SmallLettersLength  = round(PasswordLength - CapitalLettersLength - NumberLength - SpeicalLettersLength)

    if Passwordlevel == 'hard':
        # 30% = capitalLetter, 20% = number, 30% = specialLetter, remaining = smallLetter
        CapitalLettersLength  = round(PasswordLength * 0.3)
        NumberLength = round(PasswordLength * 0.2)
        SpeicalLettersLength = round(PasswordLength * 0.3)
        SmallLettersLength  = round(PasswordLength - CapitalLettersLength - NumberLength - SpeicalLettersLength)
    
    return generatePassword(CapitalLettersLength,NumberLength,SmallLettersLength,SpeicalLettersLength)

def main():
    print("Simple password generator.")
    levels = ['easy', 'medium', 'hard']
    level = input("Enter password level(easy,medium,hard)(Default easy): ")
    length =input("Enter password length(>2)(Default 10): ")
    level = level.lower() if level.lower() in levels else 'easy'
    if length == '':
        length = 10
        print("Password is: " + generate(level=level,length=length))
    else:
        try:
            length = int(length)
            print("Password is: " + generate(level=level,length=length))
        except ValueError:
            print("Error, length should be in number.")
    
if __name__ == '__main__':
    main()