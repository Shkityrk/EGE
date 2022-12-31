with open("data/17-4.txt") as f:
    a=[int(x) for x in f.readlines()]
kol=0
mx=-10**11
mn=10**10
for i in range(len(a)):
    b=a[i]
    s=[]
    s.append(1)
    s.append(b)
    for d in range(2,int(b**0.5)+1):
        if b%d==0:
            s.append(d)
            s.append(b//d)
    k=0
    for x in s:
        if len(str(x))==1 and str(x) in '2357':
            k+=1
            
    if k==2:
        kol+=1
        mx=max(mx,a[i])
        mn=min(mn, a[i])
print(kol, mx+mn)
        
        
