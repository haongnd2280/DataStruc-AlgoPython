# isalpha(): check if all the characters in the text are letters.
#            returns True if all the characters are alphabet letters (a-z)

text = "Welcome to the jungle!"
x = text.isalpha()
print(x)
for char in text:
	if char.isalpha():
		print(char, end=' ')