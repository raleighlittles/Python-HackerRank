#!/bin/python3

import sys, re

N, M = map(int, input().split())
a = []
b = ""

for i in range(0, N):
    line = input()
    a.append(line)
    
for z in zip(*a):
    b += ''.join(z)
    
output = re.sub(r'(?<=\w)([^\w]+)(?=\w)', " ", b)
print(output)
