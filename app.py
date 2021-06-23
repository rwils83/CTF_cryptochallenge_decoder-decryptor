import base64 as b
import argparse
import codecs
import string
import pdb
def check(cipher_string, char):
        #pdb.set_trace()
        if(char.upper() in cipher_string):
            pass
        else:
            print(f'[+] {char.upper()} not found in Encrypted String. Removing from used Alphabet')
            return char.upper()

def vigenere_decrypt(encrypted_string):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for character in alphabets:
        if check(encrypted_string, character) is None:
            pass
        else:
           alphabets = alphabets.replace(character, "")
    return f"""
[+] Goto https://www.dcode.fr/vigenere-cipher and enter {alphabets} as your alphabet. Then click Automatic Decrypt.
[+] If you know the Cipher Key, enter in Knowing the Key text box under Decryption method and click decrypt instead.""" 


def base64_Encode(test=None):
    if test == None:
        cleartext = raw_input("Enter the string to encode \n")
    else:
        cleartext = test
    return b.b64encode(cleartext)


def base64_Decode(test=None):
    if test == None:
        encoded_text = raw_input("Enter the string to decode \n")
    else:
        encoded_text = test
    try:
        return b.b64decode(encoded_text)
    except:
        return "Please enter a base64 encoded string"


def base32_Encode(test=None):
    if test == None:
        cleartext = raw_input("Enter the string to encode \n")
    else:
        cleartext = test
    return b.b32encode(cleartext)


def base32_Decode(test=None):
    if test == None:
        encodedtext = raw_input("Enter the string to decode \n")
    else:
        encodedtext = test
    try:
        return b.b32decode(encodedtext)
    except:
        return "Please enter a base32 encoded string"


def rot_13_encrypt(test=None):
    if test == None:
        cleartext = raw_input("Enter the string to encrypt \n")
    else:
        cleartext = test
    return codecs.encode(cleartext, "rot_13")


def rot_13_decrypt(test=None):
    if test == None:
        cleartext = raw_input("Enter the string to decrypt \n")
    else:
        cleartext = test
    return codecs.decode(cleartext, "rot_13")


def parse_args():
    description = "Encode, Decode, Encrypt, Decrypt basic CTF challenges"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-d", "--decrypt", action="store_true", help = "Decode/Decrypt")
    parser.add_argument("-e", "--encrypt", action="store_true", help = "Encode/Encrypt")
    parser.add_argument("-b64", "--base64", action="store_true", help="Use for base64 with -d or -e")
    parser.add_argument("-b32", "--base32", action="store_true", help="Use for base32 with -d or -e")
    parser.add_argument("-r13", "--rot13", action="store_true", help="Use for Rot13 with -d or -e")
    parser.add_argument("-s", "--string", action="store", help="String to encrypt/decrypt")
    parser.add_argument("-vi", "--vigenere", action="store_true", help="Decrypt vigenere cipher text")
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = parse_args()

    if args.base64 and args.decrypt:
        print(base64_Decode(args.string))
    if args.base64 and args.encrypt:
        print(base64_Encode(args.string))
    if args.base32 and args.decrypt:
        print(base32_Decode(args.string))
    if args.base32 and args.encrypt:
        print(base32_Encode(args.string))
    if args.rot13 and args.decrypt:
        print(rot_13_decrypt(args.string))
    if args.rot13 and args.encrypt:
        print(rot_13_encrypt(args.string))
    if args.vigenere:
       print(vigenere_decrypt(args.string))

