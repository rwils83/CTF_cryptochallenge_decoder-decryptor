# CTF Crypto Challenge Decoder Encoder

## What is it?

Quick Encoder/Decoder for b64, b32, r13.

## How do I use it?

Help: python3 app.py --help Must use -s, --string <stringToEncode/Decode>
Base64: use -b64, --base64 Base32: use -b32, --base32 rot13: use -r13, --rot13
Decode: use -d, --decode Encode: use -e, --encode

## What else is left to be done?

I want to add md5 and sha-256, maybe some other ones. Eventually I would like to
make a seperate thing to do braille, morse code, and other common crypto
challenge things I see on CTFs.

## How can I help?

If you see a better way to do something, want to start on the new project
pieces, want to improve docs, or know anything else like that, feel free to
contribute. All I ask is you fork the repo, and PR to the dev branch. I haven't
written tests, so right now I would manually test before merging. If you are
here for Hacktoberfest, I will ensure PRs are marked as Hacktoberfest-accepted
and will merge later so you get credit. Hacktoberfest-accepted :please accept my
PR
