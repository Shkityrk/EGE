f=open('26-119.txt')
N,L,M=map(int,f.readline().split())

a=[]
park=[0]*(L+M)
miss=0
bus=0


for i in range(N):
    st, t,type=f.readline().split()
    a.append([int(st), int(st)+int(t), str(type)])
a.sort()

for i in range(N):
    st,end, type=a[i]
    if type=='A':
        for j in range(L+M):
            if park[j]<=st:
                park[j]=end
                break
        else:miss+=1
    if type=='B':
        for j in range(L,L+M):
            if park[j]<=st:
                park[j]=end
                bus+=1
                break
        else:miss+=1
print(bus, miss)
