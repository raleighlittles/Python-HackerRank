import re
zipcode = input()

print(bool(re.match(r'(?!.*(.).\1.*(.).\2)' r'(?!.*(.)(.)\3\4)' r'[1-9]\d{5}', zipcode)))
# First regex: checks a case of alternating repeating digits
# Second regex: Checks another case of alternating repeating digits (1212, etc)
# Checks structure: must start with 1-9 but can have 0s after
