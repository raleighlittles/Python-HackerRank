import re
print(*re.split(r'[.,]+', input().strip('.,')), sep='\n')