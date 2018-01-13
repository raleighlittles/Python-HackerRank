set_A = set(map(int, input().split()))
num_other_sets = int(input())
other_sets = []
for i in range(0, num_other_sets):
    other_set = set(map(int, input().split()))
    other_sets.append(other_set)

x = all([set(s) < set_A for s in other_sets])
print(x)