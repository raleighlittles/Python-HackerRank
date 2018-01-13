n = input()
N = list(map(int, input().split()))
m = input()
M = list(map(int, input().split()))

sym_diff = []
#print(set(N).difference(set(M)))
#print(set(M).difference(set(N)))

sym_diff.append(list(set(N).difference(set(M))))
sym_diff.append(list(set(M).difference(set(N))))

sym_diff = [item for sublist in sym_diff for item in sublist]
for elem in sorted(sym_diff):
    print(elem)
    