def d(x):
    a=[]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            a.append(i)
            a.append(x//i)
    return sorted(a)
def pr(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:return 0
    return 1
k=0
for n in range(350_001,1_000_000):
    dels=d(n)
    if len(dels)!=0:
        if pr(max(dels))!=1:
            print(n,max(dels))
            k+=1
            if k>=6:break