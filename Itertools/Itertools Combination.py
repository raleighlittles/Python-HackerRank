import itertools

word, number_comb = input().split(" ")
word = sorted(word)


for i in range(1,int(number_comb) +1):
    list_comb = list(itertools.combinations(word,i))
    for j in list_comb: 
        print("".join(j))