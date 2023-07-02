f=open('schelchok/26_2__1vv2z.txt')
a,b,c=map(int,f.readline().split())
data=[]
for i in range(c):
    s=int(f.readline())
    data.append(s)
data.sort(reverse=True)
free=[b]*a
kol=0

for x in data:
    for i in range(a):
        if free[i]>=x:
            free[i]-=x
            kol+=1
            break
print(kol,sum(free))