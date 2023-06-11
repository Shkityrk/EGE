f=open('files_compege/27A_2724.txt')
n=int(f.readline())
a=[0]*131
count=0
for i in range(n):
    x=int(f.readline())
    ost=0 if x%131==0 else 131-x%131
    count+=a[ost]

    a[x%131]+=1
print(count)