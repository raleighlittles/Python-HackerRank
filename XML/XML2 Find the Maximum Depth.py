maxdepth = 0
def depth(elem, level): # Take a simple DFS approach
    global maxdepth
    # your code goes here
    level += 1
    [depth(element, level) for element in elem.getchildren()]
    maxdepth = level if level > maxdepth else maxdepth
    return maxdepth
    