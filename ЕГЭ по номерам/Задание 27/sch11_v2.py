f=open('schelchok/11_B__1vjye.txt')
n=int(f.readline())
q=[int(f.readline()) for i in range(8)]
a=[int(x) for x in f.readlines()]
ans=-10**20
for i in range(n-8):
    for j in range(len(q)):
        if a[i]*q[j]%15==0:ans=max(a[i]*q[j], ans)
    q.append(a[i])
    q.pop(0)
print(ans)

