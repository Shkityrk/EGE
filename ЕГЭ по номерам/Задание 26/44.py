f=open('data/26-44.txt')
a=[int(x) for x in f.readlines()]
a=a[1:]
c=[[] for c in range(10000//500+1)]
a.sort()
k=1

su=0
mx=0
for l in range(len(a)):
    if a[l]<=500*k:c[k].append(a[l])
    if a[l]>500*k:
        c[k+1].append(a[l])
        k+=1
for p in c:
    for i in range((len(p)//2)):
        su+=p[i]/2
        mx=max(mx,p[i]//2)

print(su,mx)
