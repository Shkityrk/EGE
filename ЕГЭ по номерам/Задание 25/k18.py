a=set([i**2 for i in range(1,10000)])
def dels(n):
    d=set()
    if n in a or n%2==0:
        for i in range(1,int(n**0.5)+1):
            if n%i==0:d|={i,n//i}
    return ([x for x in d if x%2!=0])
for n in range(55_000_000,60_000_000+1):
    d=dels(n)

    if len(d)==5:
        print(n,max(d))