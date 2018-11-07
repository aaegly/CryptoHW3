'''
Andrew Egly
HW 3 ECIES
Cryptography CS 486
Description: This program takes the contents of a file given by the command line and first encrypts using ECIES,
prints the encryption, then decrypts using ECIES and prints the original message.
'''

#used for command line arguments
import sys
# importing ecies for use in creating public/private keys with ECIES encryption
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt

'''
Main function used for implementing overall program
I could have made this smaller by splitting some things into functions,
but the overall program seemed too small to try to complicate it.
'''
def main():

	# in case a file is not input in the command line
	if (len(sys.argv) < 2):
		print ("invalid use of program")
		print ("Please add one file path as an argument for this program")
		exit()
	else:

		# generate secret key to be used for public, private key creation
		# this would be the shared secret value between the users
		k = generate_eth_key()

		# making and saving the private key
		prvhex = k.to_hex()
		print("private key", prvhex)

		# making and saving the public key
		pubhex = k.public_key.to_hex()
		print("public key", pubhex)

		# open file with the message that is being encrypted and save the message to a variable
		file = open(sys.argv[1], 'r')

		# begin encryption
		print("encrypting...")

		# read the file to a variable for use in the encryption function
		try:
			message = file.read()
		except:
			# catching invalid inputs so it doesn't crash
			print("invalid path or file")
			exit()

		# convert the message into bytes to be used in the function
		byte_message = str.encode(message)

		# save the encrypted message so that it may be sent
		secret = encrypt(pubhex, byte_message)

		#finished with encryption
		print("encrypted")

		# print the encrypted message
		print(secret)

		# begin decryption of the message
		print("decrypting...")

		# saving decrypted message in case it should be written to a file or used elsewhere
		cracked = decrypt(prvhex, secret)

		# finished decryption
		print("decrypted")

		#printing the final message after decryption
		print(cracked)

		# closing the file that was encrypted/decrypted
		file.close()

main()