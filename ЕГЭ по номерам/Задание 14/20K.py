def f(n,o):
    s=[]
    while n!=0:
        s.append(n%o)
        n//=o
    return s[::-1]
k=0
for i in range(1,10000):
    if len(f(i,5))<=4 and len(f(i,2))>=5 and f(i,16)[-1]==12:k+=1
print(k)