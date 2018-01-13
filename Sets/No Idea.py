n, m = input().split()
arr = [int(x) for x in input().split()]
A = set([int(y) for y in input().split()])
B = set([int(z) for z in input().split()])

count = [1 if x in A else -1 if x in B else 0 for x in arr]
print(sum(count))