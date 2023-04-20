from  itertools import*

f=open('files_compege/27B_2737.txt')
n=int(f.readline())
a=[0]*2000

for i in range(n):
    x=int(f.readline())
    if x<2000:a[x]+=1

c=a[1000]*(a[1000]-1)//2
for i in range(1,1000):
    c+=a[i]*a[2000-i]
print(c)
