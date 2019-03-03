import sys

def encoder(val):
    return (map(bin,bytearray(val, 'utf8')))

def myecryptkey():
    return(encoder("Prabhu Gurung"))

def encrypt(value):
    binText = encoder(value)
    myeconderKey = myecryptkey()
    
    print (binText)


  #return cypherText


arg1,arg2 = sys.argv[1:3]

if arg1.lower() == "--e":
    encrypt(arg2)
elif arg1.lower() == "--d":
    decrypt(arg2)
else: 
    print("bad argument \n : help \n encrypter [option] [value] \n option : \n --e : encrypter \n --d : decrypter")



