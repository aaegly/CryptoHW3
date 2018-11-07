# CryptoHW3
Write a Python command line program that encrypts and decrypts files based on public key cryptography.


Description: This program takes the contents of a file given by the command line and first encrypts using ECIES, prints the encryption, then decrypts using ECIES and prints the original message.

Features: this program has the encryption/decryptions feature that works with text files. It also has a few if and try statements to attempt to catch any issues that would crash the program due to faulty user input or invalid files.

Limitations: The limit to how large a message can be is only as large as a string in python, anything larger would most likely crash the program. Also, although this is meant to show how messages can be shared between people on the internet securely, it doesn't actually have a function to send messages to others. Encryption is also limited to text only.

Version: Python 3.5

Libraries: Sys- used for the file reading functions
ecies and ecies.utils- used for key generation using the ECIES algorithm with AES

I used ecies because after searching for how to implement this algorithm myself, most of the sources that I found would point me to builtins that I should use instead, or would get deeply technical to the point where I would get lost on what was being explained.

Command Line Help: (python3 CryptoHW3.py testfile.txt)
This is how I tested my code. However you use python 3.5 would be swapped in for python3, and the testfile.txt can be swapped for a test file.

Sources: key generation reference: https://github.com/paritytech/parity-ethereum/tree/master/ethkey#generate-brain-seed

used for key generation: https://pypi.org/project/eciespy/

ecies key encryption/decryption reference: https://ethereum.stackexchange.com/questions/18208/what-is-a-public-key-under-ecies-and-how-to-get-it
