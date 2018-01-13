import itertools
input_line = input()
string = input_line.split()[0]
K = input_line.split()[1]
substrings = []
x = list(itertools.permutations(string, int(K)))
for y in x:
    z = ''.join(y)
    substrings.append(z)
    
for s in sorted(substrings):
    print(s)
