import re
import email.utils 

N = int(input())

pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
for i in range(0, N):
    parsed_addr = email.utils.parseaddr(input())
    if re.search(pattern, parsed_addr[1]):
        print(email.utils.formataddr(parsed_addr)) 
    