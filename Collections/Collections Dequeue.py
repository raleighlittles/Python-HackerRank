import collections

N = int(input())

deq = collections.deque()

for i in range(0, N):
    input_line = input()
    if len(input_line.split()) == 1: 
        statement = "deq." + input_line + "(" + ")"
        eval(statement)
    else:
        command = input_line.split()[0]
        argument = input_line.split()[1]
        
        statement = "deq." + command + "(" + argument + ")"
        eval(statement)
        
print(' '.join(str(x) for x in deq))
        
        
        
        