f=open('files_compege/27B_2757.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
k=9
k23=kn23=0
count=0

for i in range(k,n):
    if a[i-k]%23==0:k23+=1
    if a[i-k]%23!=0:kn23+=1

    if a[i]%23==0:count+=k23+kn23
    if a[i]%23!=0:count+=k23
print(count)