n = int(input())
set_A = set(list(map(int, input().split())))
num_of_commands = int(input())
for i in range(0, num_of_commands):
    command = input().split()[0]
    new_set = set(list(map(int, input().split())))
    statement = "set_A." + command + "(" + "new_set" + ")"
    eval(statement)
    
print(sum(set_A))