start, end = 106868, 226868

def divs(n):
    s=[]
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)

def is_prime(x):
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))


ans=[]
for i in range(start,end+1):
    all_divs=divs(i)
    prime_divs=[b for b in all_divs if is_prime(b)]
    if len(prime_divs)==3 and prime_divs[0]*prime_divs[1]*prime_divs[2]==i:
        ans.append(i)

print(len(ans), max(ans))
