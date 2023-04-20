f=open('files_compege/27B_2725.txt')
n=int(f.readline())
a=[0]*69

for i in range(n):
    x=int(f.readline())
    a[x%69]+=1
c=0
for i in range(69):
    c+=a[i]*(a[i]-1)//2
print(c)