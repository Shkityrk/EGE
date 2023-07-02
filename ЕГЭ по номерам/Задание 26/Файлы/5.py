f=open('26-122.txt')
k,n=map(int, f.readline().split())
a=[]
for i in range(n):
    st,end=map(int,f.readline().split())
    a.append([st,end])
a.sort(key=lambda x:x[0])

house=[0]*n
last=0
for i in range(n):
    st,end=a[i]

    for j in range(n):
        if house[j]<st:
            house[j]=end+1
            last=st
            break
house=[x for x in house if x!=0]

print(len(house)/k, len([x for x in house if x>last]))