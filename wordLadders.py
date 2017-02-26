# Word Ladders!!!!
# CC, 2017

from copy import copy

all_words = {}
f = open('words.txt')

# Fill all_words with words
for word in f:
    word = word.strip()
    all_words[word] = 0

start_word = raw_input("Start word: ")
end_word = raw_input("End word: ")

paths = {word: [] for word in all_words}
to_visit = {start_word: 0}
visited = {}
result = []
ladder_found = False

"""Finds possible transformation and adds them to an array corresponding to
its parent word. (Each word in all_words will have an array, empty or not.
When end_word is found, it turns ladder_found to True --> there is a ladder
from start_word to end_word. """

while to_visit and not ladder_found:
    to_check = to_visit.copy()
    
    for word in to_check:
        to_visit.pop(word, None)
        visited[word] = 0
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + ch + word[i+1:]
                if new_word in all_words and new_word not in visited:
                    if new_word == end_word:
                        ladder_found = True
                    to_visit[new_word] = 0
                    paths[new_word].append(word)
                    

# Traces back from end_word to start_word recursively, adding word to result
def path_finder(start, end):
    for list_word in paths[end]:
        if list_word == start:
            result.append(list_word)
            return
        else:
            path_finder(start, list_word)
            if start in result:
                result.append(list_word)
                return
  
# Prints path if ladder is found, indicates no path was found otherwise
if ladder_found:
    path_finder(start_word, end_word)
    result.append(end_word)
    print '\n'.join(word for word in result)
else:
    print "No path found!"