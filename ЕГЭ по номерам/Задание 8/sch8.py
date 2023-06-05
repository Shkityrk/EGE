from itertools import *
k=0
for x in product('МИРОСЛАВ',repeat=5):
    s=''.join(x)
    if s[0]!=s[1]!=s[2]!=s[3]!=s[4]:
        s=s.replace('О','*').replace('И','*').replace('А','*')
        if (len(s)-s.count('*')>s.count('*')) and (s[0]!='*') and (not '**' in s):k+=1
print(k)