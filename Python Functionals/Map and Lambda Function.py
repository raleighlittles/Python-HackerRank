cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = []
    if n == 0:
        return fib_list
    a, b = 0, 1
    fib_list.append(a)
    while len(fib_list) < n:
        fib_list.append(b)
        a, b = b, a+b
        

    return(fib_list)