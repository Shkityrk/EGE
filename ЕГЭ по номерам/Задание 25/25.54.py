start, end = 3, 20_000
def divs(n):
    s=[]
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)

def is_prime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))


n=0
for i in range(start,end+1):
    pr=sorted(m for m in divs(i) if is_prime(m))
    if len(pr)>3:
        n+=1
print(n)