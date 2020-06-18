import base64 as b
import argparse
import codecs



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
    parser.add_argument("-b64", "--b64", action="store_true", help="Use for base64 with -d or -e")
    parser.add_argument("-b32", "--b32", action="store_true", help="Use for base32 with -d or -e")
    parser.add_argument("-r13", "--r13", action="store_true", help="Use for Rot13 with -d or -e")
    parser.add_argument("-s", "--string", action="store", help="String to encrypt/decrypt")
    args = parser.parse_args()
    return args
if __name__ == "__main__":

    args = parse_args()

    if args.b64 and args.decrypt:
        print base64_Decode(args.string)
    if args.b64 and args.encrypt:
        print base64_Encode(args.string)
    if args.b32 and args.decrypt:
        print base32_Decode(args.string)
    if args.b32 and args.encrypt:
        print base32_Encode(args.string)
    if args.r13 and args.decrypt:
        print rot_13_decrypt(args.string)
    if args.r13 and args.encrypt:
        print rot_13_encrypt(args.string)



