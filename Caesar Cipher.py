#Caesar Cipher Technique
def encrypt(text,s):
	result = ""

	
	for i in range(len(text)):
		char = text[i]

		
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result


text = input("Enter Plain Text : ")
s = int(input("Enter a Key : "))
print ("Entered Text is  : " + text)
print ("Shift Value is : " + str(s))
print ("Cipher: " + encrypt(text,s))
