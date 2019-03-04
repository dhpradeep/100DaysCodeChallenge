# Python simple encryption description program.
import sys

import itertools

def alternate(xs, ys):
    head = itertools.chain.from_iterable(zip(xs, ys))
    return itertools.chain(head, xs[len(ys):], ys[len(xs):])

def helpMessage():
    print("\nHelp message")
    print("encrypter [option] [value]")
    print("options:")
    print("\t--encrypt or -E => encrypt")
    print("\t--decrypt or -D => decrypt")
    print("\tFor example: 'encrypter -E pradeep'")

def hashcode():
    return list('my-hashcode')

def encrypt(normalText,val):
    # if(val >= 1):
    #     textlen = len(normalText)
    #     hashcodeString = hashcode()
    #     evenString = []
    #     oddString = []
    #     for i in range(textlen):
    #         if i % 2 != 0:
    #             evenString.insert(i,normalText[i])
    #         else:
    #             oddString.insert(i,normalText[i])

    #     cypherText = list(alternate(evenString,oddString))
    #     cypherText = list(alternate(cypherText,hashcodeString))
        
    #     cypherText = [''.join(i for i in cypherText)]
    #     cypherText = str(cypherText[0])
    #     val = val -1
    #     print(cypherText)
    #     return(encrypt(cypherText,val))
    # else:
    #     return normalText
    return normalText[::-1]
    
    
def decrypt(cypherText,val):
    # if(val >= 1):
    #     hashcodeString = hashcode()
    #     textlen = len(cypherText)
    #     normalText = [cypherText]
    #     normalText = list(alternate(normalText,hashcodeString))
    #     evenString = []
    #     oddString = []
    #     # for i in range(textlen):
    #     #     if i % 2 != 0:
    #     #         evenString.insert(i,normalText[i])
    #     #     else:
    #     #         oddString.insert(i,normalText[i])
    #     # normalText = list(alternate(evenString,oddString))
    #     print(normalText)
    #     return(decrypt(cypherText,val))
    # else:
    #     return cypherText
    return cypherText[::-1]

    

arg1, arg2 = sys.argv[1:3]
if(arg1.lower() == '--encrypt' or arg1.upper() == '-E'):
    print(encrypt(arg2,1))
elif(arg1.lower() == '--decrypt' or arg1.upper() == '-D'):
    print(decrypt(arg2,1))
else:
    helpMessage()
