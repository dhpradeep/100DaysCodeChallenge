import sys
import base64

key = "prabhu"
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


while True:
    try:
        arg1,arg2 = sys.argv[1:3]
    except:
        print(": help \n [option] [value] \n option : \n --e : encrypter \n --d : decrypter")
        arg1,arg2 = input().split()
        

    if arg1.lower() == "--e":
        ec =encode(key, arg2)
        print(ec)
    elif arg1.lower() == "--d":
        dc = decode(key, arg2)
        print(dc)
    else: 
        print("bad argument \n : help \n encrypter [option] [value] \n option : \n --e : encrypter \n --d : decrypter")

    if input("Press E for exit: ").lower() == "e":
        exit()

