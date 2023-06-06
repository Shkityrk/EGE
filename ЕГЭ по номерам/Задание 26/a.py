f=open('data/26_8512.txt')
k=int(f.readline())
n=int(f.readline())

a=[]
for i in range(n):
    st,end=map(int,f.readline().split())
    a.append([st,end])
a.sort()
last=0
cnt=0
cell=[-1]*k
for i in range(n):
    st,end=a[i]
    for j in range(k):
        if st>=cell[j]+1:
            cell[j]=end
            cnt+=1
            if st!=a[i-1][0] and i>0:
                last=j+1
            break
print(cnt,last)