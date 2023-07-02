def f(n):
    s=''
    while n!=0:
        s+=str(n%3)
        n//=3
    return s[::-1]

mn=10**20
for n in range(1,1000):
    s=f(n)
    if n%3==0:
        s=s+s[-2:]
    else:
        ost= f((n%3)*5)
        s=s+ost
    r=int(s,3)
    if r>=146:mn=min(mn,r)
print(mn)