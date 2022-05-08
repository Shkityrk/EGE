start, end = 536792, 604298
def divs(n):
    s=[]
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)

def is_prime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

c=0
mx=-1
mx_i=0
for i in range(start,end+1):
    d=divs(i)
    pr= sorted([l for l in d if is_prime(l)])
    if len(pr)==3 and pr[0]*pr[1]*pr[2]==i and pr[0]%10==pr[1]%10==pr[2]%10:
        c+=1
        if pr[2]-pr[0]>mx:
            mx=pr[2]-pr[0]
            mx_i=i
print(c, mx_i)