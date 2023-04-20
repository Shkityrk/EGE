f=open('files_compege/27B_2723.txt')
n=int(f.readline())
k=0
for i in range(n):
    x=int(f.readline())
    if x%19==0:k+=1
print(k*(k-1)*(k-2)//6)