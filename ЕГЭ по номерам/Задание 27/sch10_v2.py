f=open('schelchok/10_B__1vjyc.txt')
n=int(f.readline())
q=[int(f.readline()) for i in range(6)]
a=[int(x) for x in f.readlines()]
ans=-10**20
for i in range(n-6):
    for j in range(len(q)):
        ans=max(a[i]*q[j], ans)
    q.append(a[i])
    q.pop(0)
print(ans)

