import itertools
N = int(input())
letters_list = input().split()
K = int(input())
letters_dict = itertools.combinations(''.join(letters_list), K)
counts, total = 0, 0
for tup in list(letters_dict):
    total += 1
    if 'a' in tup:
        counts += 1
        
print(counts/total)        
        
