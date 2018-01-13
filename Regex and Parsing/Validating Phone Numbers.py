import re

N = int(input())
for i in range(0, N):
    # Must start with a 7, 8, or 9 according to the problem, must only contain 10 digits total
    print('YES') if re.match(r'[789]\d{9}$', input()) else print('NO') 
        