import collections

n = int(input())

my_dict = collections.OrderedDict()

for i in range(0, n):
    word = input()
    if (word not in my_dict.keys()):
        my_dict[word] = 1
        
    else:
        my_dict[word] += 1
    
print( len(my_dict.keys()))
print(*my_dict.values())
    