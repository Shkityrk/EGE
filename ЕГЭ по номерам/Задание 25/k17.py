a=set([i**2 for i in range(1,100000)])
def dels(n):
    d=set()
    if n in a:
        for i in range(2,int(n**0.5)+2):
            if n%i==0:d|={i,n//i}
    return sorted(d)
for n in range(106_732_567,152673836+1):
    d=dels(n)
    if len(d)==3:
        print(n,max(d))