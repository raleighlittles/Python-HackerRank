import re
# Had to look this one up. See: https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression

thousands = 'M{0,3}' # matches anything like M, MM, etc
hundreds = '(CM|CD|D?C{0,3})' #matches anything like: C, C, CCC, CD, D, DC, etc, and CM (900)
tens = '(XC|XL|L?X{0,3})' # matches anything like: X, XX, XXX, XL, .., up to XC (90)
digits = '(IX|IV|V?I{0,3})' # the individual roman numeral digits
print(bool(re.match(thousands + hundreds + tens + digits + '$', input()))) # Use the $ to match the end of the string

