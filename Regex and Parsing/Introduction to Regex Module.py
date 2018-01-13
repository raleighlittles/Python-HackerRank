import re
T = int(input())

for i in range(0, T):
    string = input()
    # Regex has to match: (plus or minus) (a digit, 'd' character class) (a decimal point '.') (another digit)
    print(bool(re.match(r"^[-+]?\d*\.\d+$",string)))