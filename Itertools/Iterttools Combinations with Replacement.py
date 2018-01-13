import itertools

s, k = input().split()

for c in itertools.combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))