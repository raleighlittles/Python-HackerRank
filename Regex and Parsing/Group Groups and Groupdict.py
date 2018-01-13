import re
# Can't use '\w' since you dont want to match on underscore..
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)