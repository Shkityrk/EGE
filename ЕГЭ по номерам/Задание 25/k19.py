a=set([i**2 for i in range(1,15000)])
def dels(n):
    d=[]
    if n in a or n%2==0:
        for i in range(1,int(n**0.5)+2):
            if n%i==0 and i%2==0:d.append(i)
            if n % (n//i) == 0 and (n//i) % 2 == 0: d.append((n//i))
    return sorted(set(d))
for n in range(113_000_000,114_000_000+1):
    d=[int(x) for x in dels(n) if x%2==0]
    if len(d)==3:
        print(n,d[1])