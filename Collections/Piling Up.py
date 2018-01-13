import collections
T = int(input())

for i in range(0, T):
    num_cubes = int(input())
    sidelengths = collections.deque(map(int, input().split()))
    can_stack = True
    
    while len(sidelengths) != 1:
        if sidelengths[0] >= sidelengths[1]:
            sidelengths.popleft()
            
        elif sidelengths[-1] >= sidelengths[-2]:
            sidelengths.pop()
        
        else:
            can_stack = False
            break
            
    print('Yes') if can_stack else print('No')  
            
    