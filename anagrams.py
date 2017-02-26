# Anagrams
# CC, 2017

d = {}

# Open file
f = open('words.txt')

for word in f:
    word = word.strip()
    
    key = tuple(sorted(word))
    if d.has_key(key):
        d[key] = d[key] + (word,)
    else:
        d[key] = (word,)

print d