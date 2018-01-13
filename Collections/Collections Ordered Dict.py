import collections
inventory = collections.OrderedDict()
N = int(input())
for i in range(0, N):
    input_line = input()
    item_name, price = input_line.split()[:-1], int(input_line.split()[-1])
    if str(' '.join(item_name)) in inventory:
        inventory[' '.join(item_name)] += price
    else:
        inventory[' '.join(item_name)] = price
         
    
for key in inventory:
    print(key, inventory[key])
    