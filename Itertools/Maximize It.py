import itertools

k,m = map(int,input().split())

L = [list(map(int, input().split()))[1:] for i in range(k)]

result = 0
for i in itertools.product(*L):
    r = 0
    for n in i:
        r += n**2
        
    if result < r % m:
        result = r % m
print(result)