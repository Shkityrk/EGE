f=open('3_26.txt')
k=int(f.readline())
n=int(f.readline())

count=0
time=0
a=[]
boxes=[0]*k
boxes_time=[[0]*k for i in range(1441)]
for i in range(n):
    st,end=map(int,f.readline().split())
    a.append([st,end])
a.sort()

for i in range(n):
    st,end=a[i]
    for j in range(k):
        if boxes[j]<=st:
            boxes[j]=end+1
            count+=1

            for t in range(st,end):
                boxes_time[t][j]=1

            break
print(count)
for t in range(1441):
    if t!=0:
        if sum(boxes_time[t])>0:time+=1
print(time)