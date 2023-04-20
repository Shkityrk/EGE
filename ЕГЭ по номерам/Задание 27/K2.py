f=open('files_compege/27A_2720.txt')
n=int(f.readline())
k=k0=0

for i in range(n):
    x=int(f.readline())
    if x%7==0:k+=1
    else:k0+=1
print(k*(k-1)//2+k*k0)