f=open('1_26.txt')
k=int(f.readline())
n=int(f.readline())

count = 0
last_start = -1
last_nomer = -1
a=[]

for i in range(n):
    st,end=map(int, f.readline().split())
    a.append([st,end])
a.sort()
boxes=[0]*k
for pas in a:
    start=int(pas[0])
    end=int(pas[1])

    for i in range(k):
        if boxes[i]<=start:
            boxes[i]=end+1
            count+=1

            if start>last_start:
                last_start=start
                last_nomer=i+1
            break
print(count,last_nomer)