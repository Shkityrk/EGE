from fnmatch import *
def div(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for x in range(10**7):
    if fnmatch(str(x),'?8*8*?8') and x%6==0 and x%7==0 and x%8==0:
        print(x, sum(div(x)))
