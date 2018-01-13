import re
S = input()
vowels = 'AEIOU'
while (S[len(S)-1] in vowels) or (S[len(S) - 1] in vowels.lower()):
    S = S[:-1]
    
while (S[0] in vowels) or(S[len(S) -1] in vowels.lower()):
    S = S[1:]
    
matcher = re.findall(r'[aeiou]{2,}', S, re.I)
print(*matcher, sep='\n') if matcher else print(-1)
    