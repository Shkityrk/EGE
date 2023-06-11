f=open('files_kompege/26_2480.txt')
n=int(f.readline())

road=[0]*2_000_000

for i in range(n):
    start,end=map(int, f.readline().split())
    for j in range(start,end):
        if road[j]==0:road[j]=1
k=0
m=0
for i in range(len(road)):
    if road[i]==1:
        k+=1
    else:k=0

s=''.join(str(x) for x in road)
s=s.split('0')
ans=[x for x in s if len(x)!=0]
print(len(max(ans)))
