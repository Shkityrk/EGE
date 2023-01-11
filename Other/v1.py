from itertools import product
def f(n):
    l=''
    while n!=0:
        l+=str(n%12)
        n//=12
    l=l[::-1]
    while l[0]==0:
        l=l[1:]
    return int(l[0])

k=0
for x in product('0123456789', repeat=6):
    s=''
    for i in range(len(x)):
        s+=x[i]
    n=int(s)
    if n!=0:
        if n%f(n)==0:k+=1
    print(k)

print(k)