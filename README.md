# CTF Crypto Challenge Decoder Encoder 
## What is it?
A basic tool for some of the CTF Crypto challenges I see. I wanted a tool I could just use to make life a little easier when doing the basic challenges instead of spending time on google and other websites. 
## How do I use it?
└─$ python3 app.py --help                                                 
usage: app.py [-h] [-d] [-e] [-b64] [-b32] [-r13] [-s STRING] [-vi] [-m] [-P PASS_LIST]

Encode, Decode, Encrypt, Decrypt basic CTF challenges

optional arguments:
  -h, --help            show this help message and exit
  -d, --decrypt         Decode/Decrypt
  -e, --encrypt         Encode/Encrypt
  -b64, --base64        Use for base64 with -d or -e
  -b32, --base32        Use for base32 with -d or -e
  -r13, --rot13         Use for Rot13 with -d or -e
  -s STRING, --string STRING
                        String to encrypt/decrypt
  -vi, --vigenere       Decrypt vigenere cipher text
  -m, --md5             Performs very simple md5 dictionary attack. Use -P for wordlist
  -P PASS_LIST, --pass_list PASS_LIST
                        Enter a password file

## What else is left to be done?
I want to add sha-256, maybe some other ones. Eventually I would like to make a seperate thing to do braille, morse code, and other common crypto challenge things I see on CTFs, or at least add that functionality to this script.
## How can I help?
If you see a better way to do something, want to start on the new project pieces, want to improve docs, or know anything else like that, feel free to contribute. To contribute please see the CONTRIBUTIONS.md file. If you are here for Hacktoberfest, I will ensure PRs are marked as Hacktoberfest-accepted and will merge later so you get credit. 
