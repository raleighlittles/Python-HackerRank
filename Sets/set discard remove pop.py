n = int(input())
s = set(map(int, input().split())) 
num_of_commands = int(input())

for i in range(0, num_of_commands):
    command = input()
    if (command == "pop"):
        eval("s.pop()")
    else:
        statement = "s." + command.split()[0] + "(" + command.split()[1] + ")"
        eval(statement)
        
print(sum(list(s)))