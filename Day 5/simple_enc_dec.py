# Python simple encryption description program.
import sys

def helpMessage():
    print("\nHelp message")
    print("encrypter [option] [value]")
    print("options:")
    print("\t--encrypt or -E => encrypt")
    print("\t--decrypt or -D => decrypt")
    print("\tFor example: 'encrypter -E pradeep'")

def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

arg1, arg2 = sys.argv[1:3]
key = "This_is_my_key"
if(arg1.lower() == '--encrypt' or arg1.upper() == '-E'):
    print(encrypt(key,arg2))
elif(arg1.lower() == '--decrypt' or arg1.upper() == '-D'):
    print(decrypt(key,arg2))
else:
    helpMessage()
