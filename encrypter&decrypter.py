import sys
import time
from cryptography.fernet import Fernet 		#SYMMETRIC ENCRYPTION
import rsa 									#ASYMMETRIC ENCRYPTION

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END ,WARNING = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\033[93m'
def fancyDisplay(buffer, color = WARNING):
	sys.stdout.write(color)
	for i in buffer:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)
	sys.stdout.write(WHITE)
	return


fancyDisplay(""" 
			S Y M M E T R I C/E N C R Y P T I O N
	""", RED)
fancyDisplay("\nEnter message : ", YELLOW)
symmetric_message = input() 										# MESSAGE FOR ENCRYPTION

key = Fernet.generate_key()
fernet = Fernet(key)												# encryption key generation

fancyDisplay("""
				ENCRYPTION""", GREEN)
encode = fernet.encrypt
encMessage = encode( symmetric_message.encode())
strmessage = str(encode( symmetric_message.encode()))
print ("\nSYM encrypted : ", strmessage[2:-1])							# display encrypted message

fancyDisplay("""
				DECRYPTION""", GREEN)
decMessage = fernet.decrypt(encMessage).decode()
print ("\nSYM decrypted : ", decMessage)							# display decrypted message


fancyDisplay ("""
			A S Y M M E T R I C/E N C R Y P T I O N
	""", RED)
fancyDisplay("\nEnter message : ", YELLOW)
asymmetric_message = input()
publicKey, privateKey = rsa.newkeys(512)							# keys generation
encMessage = rsa.encrypt(asymmetric_message.encode(),publicKey)
strmessage1 = str(rsa.encrypt(asymmetric_message.encode(),publicKey))

fancyDisplay("""
				ENCRYPTION""", GREEN)
print ("\nASYM encrypted : ", strmessage1[2:-1])

fancyDisplay("""
				DECRYPTION""", GREEN)
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print ("\nASYM decrypted : ", decMessage, "\n")