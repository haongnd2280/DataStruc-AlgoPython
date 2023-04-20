# Note: All string methods returns new values. They do not change the original string.
#       => Accessor method.

# join: takes all items in an iterable and joins them into one string, using a hash character
#       as separator.
# join: nối
my_tuple = ("John", "Peter", "Vicky")
x = "#".join(my_tuple)
print(x)
x = ' '.join(my_tuple)
print(x)
x = "\n".join(my_tuple)
print(x)

my_tuple = ['hello', 'world', 'this', 'is', 'me']
print(' '.join(my_tuple))

# Note: When using dictionary as an iterable, the returned values are the keys, not values.
my_dict = {"name": "John", "country": "Norway"}
separator = " TEST "

x = separator.join(my_dict)
print(x)
x = "\n".join(my_dict)
print(x)