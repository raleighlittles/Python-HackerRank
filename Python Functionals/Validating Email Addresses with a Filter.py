import re
def fun(s):
    # return True if s is a valid email, else return False
    # Even though this is a filter challenge, it can easily be done using regex
    return re.match(r'^[a-z][\w-]*@[a-z0-9]+\.[a-z]{1,3}$', s, re.I)
    