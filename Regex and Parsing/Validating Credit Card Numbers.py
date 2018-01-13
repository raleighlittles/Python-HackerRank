import re

N = int(input())
# Starts with 4 or 5 or 6, consists of either 4 groups of 4 (split by a hyphen) or no groups at all
structure_check = r'[456]\d{3}(-?\d{4}){3}$'
# No digit repeats more than 4 times
no_four_repeats = r'((\d)-?(?!(-?\2){3})){16}'
filters = structure_check, no_four_repeats
for i in range(0, N):
    cc_num = input()
    print('Valid') if all(re.match(f, cc_num) for f in filters) else print('Invalid')
    