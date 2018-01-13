import re
N = int(input())
# Declare the patterns
no_repeats = r'(?!.*(.).*\1)' 
two_plus_uppercase = r'(?=(?:.*[A-Z]+){2,})'
three_plus_digits = r'(?=(?:.*\d){3,})'
ten_alphanumeric = r'[\w]{10}'
filters = [no_repeats, two_plus_uppercase, three_plus_digits, ten_alphanumeric]

for i in range(0, N):
    uid = input()
    print('Valid') if all([re.match(f, uid) for f in filters]) else print('Invalid')