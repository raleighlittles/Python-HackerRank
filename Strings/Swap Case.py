def swap_case(s):
    t = ''
    for char in s:
        if char.islower():
            t += char.upper()
        else:    
            t += char.lower()
    return t