f=open('3_26.txt')
k=int(f.readline())
n=int(f.readline())

data=[]
boxes=[0]*k
count=0
last_num=0

for i in range(n):
    st,end=map(int,f.readline().split())
    data.append([st,end])

data.sort(key=lambda x:x[0])

for i in range(n):
    st,end=data[i]

    for j in range(k):
        if boxes[j]<=st:
            boxes[j]=end+1
            count+=1
            last_num=j
            break
print(count,last_num+1)