N = int(input())

for i in range(N):
    line = input()
    # No need to even use regex for this, string's replace() method will do
    while (' && ' in line) or (' || ' in line):
        line = line.replace(' && ', ' and ')
        line = line.replace(' || ', ' or ')
        
    print(line)    