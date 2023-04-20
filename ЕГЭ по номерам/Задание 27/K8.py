f=open('files_compege/27B_2733.txt')
n=int(f.readline())
a=[0]*80
b=[0]*80

for i in range(n):
    x=int(f.readline())
    if x>50000:b[x%80]+=1
    else:a[x%80]+=1

c=0
c+=b[0]*(b[0]-1)//2+b[40]*(b[40]-1)//2
for i in range(1,39+1):
    c+=b[i]*b[80-i]

c+=b[0]*a[0]+b[40]*a[40]
for i in range(1,39+1):
    c+=b[i]*a[80-i]
    c+=a[i]*b[80-i]
print(c)