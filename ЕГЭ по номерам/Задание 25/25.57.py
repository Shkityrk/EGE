start ,end = 412567, 473265
def divs(n):
    s=[]
    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)

    return sorted(s)

def is_prime(x):
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))

kol=0
su=0
for i in range(start,end+1):
    d=divs(i)
    pr = sorted([m for m in d if is_prime(m)])
    if len(pr)==2 and pr[0]*pr[1]==i and pr[0]!=pr[1]:
        kol+=1


print('average=', su/kol)
print('kol=', kol)

