def f(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i%2==0:s.append(i)
            if (n//i)%2==0:s.append(n//i)

    return sorted(set(s))

for n in range(1204300,1204380+1):
    r = f(n)
    if len(r)>0:
        if sum(r)%10==0:
            print(n,sum(r))