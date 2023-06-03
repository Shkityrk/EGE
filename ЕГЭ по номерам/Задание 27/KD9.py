f=open('files_compege/27B_2757.txt')

n=int(f.readline())
k=9
a=[int(f.readline()) for i in range(n)]

k23=kn23=0
countB=0

for i in range(k,n):
    if a[i-k]%23==0:k23+=1
    if a[i-k]%23!=0:kn23+=1

    if a[i]%23==0:countB+=k23+kn23
    if a[i]%23!=0:countB+=k23
print(countB)