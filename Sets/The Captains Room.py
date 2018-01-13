import collections

K = int(input())
room_numbers = list(map(int, input().split()))
freq_counts = collections.Counter(room_numbers)
for key, value in freq_counts.items():
    if value != K:
        print(key)