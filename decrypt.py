import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file=='voldemort.py' or file=='thekey.key' or file=='decrypt.py':
		continue
	if os.path.isfile(file):
		files.append(file)

with open('thekey.key','rb') as key:
	skey=key.read()
userphrase=input("Enter the secret phrase to decrypt your files : ")
if userphrase=='coffee':
	for file in files :
		with open(file,'rb') as thefile:
			contents = thefile.read()
		contents_dec = Fernet(skey).decrypt(contents)
		with open(file,'wb') as thefile:
			thefile.write(contents_dec)
	print("Congrats, your files have been decrypted")
else :
	print("Sorry, wrong secret Phrase")
