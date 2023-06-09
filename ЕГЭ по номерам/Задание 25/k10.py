def f(n):
    s=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i%2==0:s.append(i)
            if (n//i)%2==0:s.append(n//i)

    return sorted(set(s))

for n in range(500001,500100):
    r = f(n)
    for i in r:
        if i%10==8 and i!=8:
            print(n,i)
            break
