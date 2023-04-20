text = "Hello, welcome to my world."
x = text.find("welcome")
print(x)

# "find" method: find the first occurrence (index) of the specified value.
#                return -1 if the value if not found.
#                is almost the same as "index", but index raise an exception if the value if not found.
# string.find(value, start, end)
x = text.find("e")
print(x)

x = text.find("e", 5, 10)

print(text.find("q"))
print(text.index("q"))

