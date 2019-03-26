import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def GetInput(input):
	print input
	return input

def encryption(key, cipher):
	renderMessage(key, cipher, mode)
def decryption(key, cipher):
	renderMessage(key, cipher, mode)

def renderMessage(key, cipher, mode):
	translated = []
	index = 0
	key = key.upper()

	for char in cipher:
		number = LETTERS.find(char.upper())
		if number != -1:
			if mode == '-e':
				number += LETTERS.find(key[index])
			elif mode == '-d':
				number -= LETTERS.find(key[index])

			number %= len(LETTERS)

			if char.isupper():
				translated.append(LETTERS[number])
			if char.islower():
				translated.append(LETTERS[number].lower())

			index += 1
			if index == len(key):
				index = 0
		else:
			translated.append(char)

	print translated
	return translated


##MAIN##

#Accept input from stdin
cipher = GetInput(sys.stdin.readline())
#mode and key will be supplied everytime
#the only thing to fix is whether input is accepted through typing or file
mode = sys.argv[1]
key = sys.argv[2]

if mode == '-e':
	render = encryption(key, cipher)
elif mode == '-d':
	render = decryption(key, cipher)

print render