import re

S = input()
k = input()

starting_index = 0

matcher = re.search(k,S)
if matcher != None:
    while matcher:
        print((matcher.start() + starting_index , matcher.end() + starting_index - 1))
        starting_index += matcher.start() + 1
        matcher = re.search(k, S[starting_index:])
        
else: print((-1,-1))