import operator

def product(fracs):
    t = reduce(operator.mul , fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator