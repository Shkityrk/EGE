f=open('26-111.txt')
k=int(f.readline())
n=int(f.readline())

a=[]
boxes=[0]*k
count=0
last=0

for i in range(n):
    st,end=map(int,f.readline().split())
    a.append([st,end])
a.sort()

for i in range(n):
    st,end=a[i]
    for j in range(k):
        if boxes[j]<st:
            boxes[j]=end
            count+=1
            last=j+1
            break
print(count,last)