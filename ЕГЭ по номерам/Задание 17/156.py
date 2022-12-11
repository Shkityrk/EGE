with open("data/17-2.txt") as f:
    a = [int(x) for x in f.readlines()]
mx=-10**10
k=0
n=10**10
for i in range(len(a)):
    mx=max(a[i],mx)
for i in range(len(a)):
    if a[i]==mx:
        k+=1
        n=min(n,i)
print(k,n+1)
