import re

for i in range(int(input())): # In this case the only valid color codes we want happen on lines that end in a semi colon
    match = re.findall(r"(\#[a-f0-9]{3,6})[\;\,\)]{1}", input(), re.I) #ignore case, since hex is both capital and lowercase
    if match:
        for j in list(match):
            print(j)