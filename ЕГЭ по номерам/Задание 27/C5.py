f=open('course/5.txt')
n=int(f.readline())

a=[int(x) for x in f.readlines()]
k=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]%19==0 and a[j]%19==0 and a[k]%19==0:k+=1
print(k)