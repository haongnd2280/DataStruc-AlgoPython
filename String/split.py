# split: split a string into a list, where each word is a list item.
#        we can specify a separator, default separator is any whitespace.
# string.split(separator, maxsplit)

text = "Welcome to the jungle!"
x = text.split()
print(x)

text = "Hello, my name is Peter, I am 26 years old."
x = text.split(", ")
print(x)
x = text.split(" ")
print(x)

text = "apple#banana#orange#cherry"
x = text.split("#")
print(x)
# setting the maxsplit parameter to 1, will return a list with 2 elements.
x = text.split("#", 1)
print(x)
x = text.split("#", 2)
print(x)

# eliminate non-alpha character
text = "Welcome to the jungle!"
x = text.isalpha()
print(x)
for char in text:
	if char.isalpha():
		print(char, end=' ')