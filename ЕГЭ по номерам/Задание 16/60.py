def f(n):
    if n>25: return n*n+4*n+3
    if n<=25 and n%3==0: return f(n+1)+2*f(n+4)
    if n <= 25 and n % 3 != 0: return f(n+2)+3*f(n+5)
kol=0
for n in range(1,1001):
    k=0
    l=f(n)
    while l!=0:
        k+=l%10
        l//=10
    if k%24==0:
        kol+=1
print(kol)