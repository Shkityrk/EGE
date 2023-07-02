f=open('26-125.txt')
d,p=map(int,f.readline().split())
a=[]
kotel=[0]*p

for i in range(d):
    time, kol=map(int,f.readline().split())
    if kol>1:
        a.append([time, kol//2])
a.sort()

ans1=0
ans2=0

for i in range(len(a)):
    time, kol=a[i]
    for j in range(p):
        if kotel[j]<=time:
            kotel[j]=time+ kol if kotel[j]==0 else time+kol+2
            ans1+=kol if kotel[j]<=1440 else 1440-time-2
            ans2=max(ans2,kol if kotel[j]<=1440 else 1440-time-2)
            break
print(ans1,ans2)