f=open('27-37a.txt')
n=int(f.readline())
summ=0
a=[int(x) for x in f.readlines()]
b=set(a)

for i in range(n):
    for j in range(i+1,n):
            if a[i]+a[j] in b:summ+=1
print(summ)