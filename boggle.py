# Boggle oggle
# CC, 2017

from copy import copy

board = [['u', 'n', 't', 'h'],
         ['g', 'a', 'e', 's'],
         ['s', 'r', 't', 's'],
         ['h', 'm', 'i', 'a']]
visited = []

# Load words.txt to all_words and build dictionary of word fragments/prefixes
all_words = {}
word_fragments = set()
f = open('words.txt')
for word in f:
    word = word.strip()
    all_words[word] = 0
    for i in range(len(word)):
        word_fragments.add(word[:i + 1])


# Method to print board
def print_board(board):
    for row in range(len(board)):
        print ' '.join(x for x in board[row])


# Add positions of the board into position_list
position_list = {}
for row in range(len(board)):
    for col in range(len(board[row])):
        position = tuple([row, col])
        position_list[position] = board[row][col]


# Find possible moves for all positions and put in a dictionary
def find_positions():
    result = {position: [] for position in position_list}
    for position in position_list:
        r = position[0]
        c = position[1] # row = x, col = y when position = (x, y)
        possibles = [(r - 1, c - 1), (r, c - 1), (r + 1, c - 1), (r - 1, c), 
                     (r + 1, c), (r - 1, c + 1), (r, c + 1), (r + 1, c + 1)]
        for pos in possibles:
            if 0 <= pos[0] < 4 and 0 <= pos[1] < 4:
                result[position].append(pos)
    return result
    

# Initialize word_list to hold words, use set() to make sure only one of
# multiple entries is added
word_list = {position: set() for position in position_list}


# Turns the word array of tuples to corresponding characters on board
def make_word(path):
    return ''.join(position_list[position] for position in path)
    

# Search by putting tuple position in array, i.e. path = [(x, y)]
def search(path):
    word = make_word(path)

    if word not in word_fragments:
        return
    
    if word in all_words:
        word_list[path[0]].add(tuple(path))
    
    # Check positions from the right of word path, i.e. end of word
    for position in valid_options[path[-1]]:
        if position not in path:
            search (path + [position])


# Search for words for each letter in the table
def find_words():
    for position in position_list:
        search([position])
        
        
print_board(board)
valid_options = find_positions()
find_words()

for position in word_list:
    print 'Words found starting from %s at %s' % (position_list[position], position)
    print [make_word(word) for word in word_list[position]], '\n'