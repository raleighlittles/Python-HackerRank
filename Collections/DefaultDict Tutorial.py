import collections
n, m = map(int, input().split())

words_dict_a = collections.defaultdict(list)
words_dict_b = collections.defaultdict(list)

for i in range(0, n):
    word_a = input()
    words_dict_a[word_a].append(i+1) 

for j in range(0, m):
    word_b = input()
    words_dict_b[word_b].append(j+1)

for word in words_dict_b:
    if word in words_dict_a:
        print(' '.join([str(x) for x in words_dict_a[word]]))
    else:
        print('-1')

        
