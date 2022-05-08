start, end = 485617, 529678
def divs(n):
    s=[]
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)

def is_prime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

razn=10**10
pr0_max=0
pr1_max=0

c=0
num=0
for i in range(start,end+1):
    d=divs(i)
    pr=sorted(l for l in d if is_prime(l))
    if len(pr)==3 and pr[0]*pr[1]*pr[2] ==i and pr[0]!=pr[1]!=pr[2]  and pr[0]%10==pr[1]%10==pr[2]%10:
        c+=1
        if pr[2]-pr[0]<razn:
            razn=pr[2]-pr[0]
            m=i
print(c,m)
