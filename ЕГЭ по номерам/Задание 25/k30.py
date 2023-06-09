from fnmatch import *
k=0
def f(n):
    s=0
    while n !=0:
        s+=n%10
        n//=10
    return s


for n in range(700_001,10**7):
    if n%13==0:
        if not(fnmatch(str(n),'*0??3*')) and not(fnmatch(str(n),'*4??2')) and not(fnmatch(str(n),'*1*')):
            print(n,f(n))
            k+=1
            if k>=5:break
