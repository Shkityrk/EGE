def f(n):
    s=[]
    s.append(1)
    if n%2!=0:s.append(n )
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0 and i%2!=0:s.append(i)
        if (n//i)%2!=0:s.append(n//i)
    return len(s)
for n in range(50000000,60000001):
    r=f(n)
    if r==5:
        print(n)