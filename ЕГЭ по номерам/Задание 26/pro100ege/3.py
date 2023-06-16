f=open('3_26.txt')
k=int(f.readline())
n=int(f.readline())

a=[]
boxes=[0]*k
count=0
minute=[0]*1440
for i in range(n):
    st,end=map(int, f.readline().split())
    a.append([st,end])
a.sort()

for i in range(n):
    st,end=a[i]
    for j in range(k):
        if boxes[j]<=st:
            boxes[j]=end+1
            count+=1
            for m in range(st,end):
                minute[m]+=1
            break

print(count)

maxkol=max(minute)
ans=0
for i in range(len(minute)):
    if minute[i]==maxkol:ans=i
print(ans)