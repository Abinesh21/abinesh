alpha = str(input())
if alpha.isalpha():
	if alpha in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
		print("Vowel")
	else:
		print("Consonant") 
else:
	print("invalid")
