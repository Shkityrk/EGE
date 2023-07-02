f=open('schelchok/26_3__1vv31.txt')
a=int(f.readline())
b=int(f.readline())
data=[]
cell=[0]*a
kol=0
last_cell=0

for i in range(b):
    st,end=map(int, f.readline().split())
    data.append([st,end])
data.sort()
print(data)

for i in range(b):
    st,end=data[i]
    for j in range(a):
        if st>=cell[j]:
            cell[j]=end+1
            kol=0
            last_cell=j+1
    break
print(kol, last_cell)