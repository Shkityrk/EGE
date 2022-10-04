from fnmatch import *

def div(x):
    s=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            s.add(i)
            s.add(x//i)
    return sorted(s)

for x in range(0, 10**7, 217):
    if fnmatch(str(x), '27?7*'):
        print(x,sum([i for i in div(x) if i%2!=0]))
