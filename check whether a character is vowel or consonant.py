alpha = str(input("Input a letter of the alphabet: "))
if alpha.isalpha():
	if alpha in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
		print("vowel")
	else:
		print("consonant") 
else:
	print("invalid")
