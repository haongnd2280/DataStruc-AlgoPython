freq = {}
filename = 'C:\\Users\\admin\\OneDrive\\sonnet29.txt'

for piece in open(filename).read().lower().split():   # piece = word 
    # only consider alphabetic characters within this piece
    word = ''.join(c for c in piece if c.isalpha())   # remove all non-alphabetic character 
    if word:                                          # require at least on alphabetic character 
        freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0

for (w, c) in freq.items():                           # (key, value) tuples represent (word, count)
    if c > max_count:
        max_word = w
        max_count = c

# print all the words and their associated count to the screen
for (w, c) in freq.items():
    print("{0}: {1}".format(w, c))

print('The most frequent word is: ', max_word)
print('Its number of occurrences is: ', max_count)


