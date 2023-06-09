def f(n):
    s=[]
    if n%2==0:s.append(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i%2==0:s.append(i)
            if (n//i)%2==0:s.append(n//i)

    return sorted(set(s))

for n in range(190201,190261):
    r = f(n)
    if len(r)==4:
        print(r[-1],r[-2])