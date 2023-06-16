f=open('3_26.txt')
k=int(f.readline())
n=int(f.readline())

a=[]
boxes=[0]*k
boxes_time=[0]*k

count=0

for i in range(n):
    st,end=map(int,f.readline().split())
    a.append([st,end])

a.sort()

for i in range(n):
    start=int(a[i][0])
    end=(a[i][1])
    for j in range(k):
        if boxes[j]<=start :
            boxes[j]=end+1
            count+=1
            boxes_time[j]+=end-start
            break
num=0
print(count)
max_time=-10**20
for i in range(k):
    if boxes_time[i]>max_time:
        max_time=boxes_time[i]
        num=i+1
print(num)

