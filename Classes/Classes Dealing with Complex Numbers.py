# Python has built-in support for complex number objects: https://docs.python.org/3/c-api/complex.html
class Complex(complex): # Subclass
    # The traditional operator overload
    def mod(self):
        return Complex(complex.__abs__(self))
    
    def __str__(self):
        return '{0.real:.2f}{0.imag:+.2f}i'.format(self) # display in A.00+B.00i format
    
    def __add__(self, number):
        return Complex(complex.__add__(self, number))
    
    def __sub__(self, number):
        return Complex(complex.__sub__(self, number))
    
    def __mul__(self, number):
        return Complex(complex.__mul__(self, number))
    
    def __truediv__(self, number): # Python3 uses truediv as the name of the '/' operator, whereas python2 just calls this 'div'
        return Complex(complex.__truediv__(self, number))
    
    
    
