def f(n):
    d=set()
    if n%2==0:d.add(2)
    for i in range(1,int(n**0.5)+1):
        if n%i==0 and 2**(i-1)%i==1:
            d.add(i)
            
    return sorted(d)

mx=0
for i in range(2, 20000):
    mx=max(mx,len(f(i)))

for i in range(2, 20000):
    if len(f(i))==mx:
        print(i,(f(i)))
        
        
