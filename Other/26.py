f=open('26__1vpyg.txt')
n,k=map(int,f.readline().split())

a=[]
for i in range(n):
    s,g=map(int,f.readline().split())
    s=int(s)
    g=int(g)
    cost=int(g/s)
    a.append([cost,s,g])
a.sort(key=lambda x:(x[0],-x[1]))
print(a)
V=0
V_max=0
max_cost=0
for i in range(k):
    c,v,s=a[i]
    V+=v
    if v>V_max:
        V_max=v
        max_cost=s
print(V,max_cost)
