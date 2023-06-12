f=open('schelchok/27-6a__1vjmj.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
k=[0]*34
count=0

for i in range(n):
    x=a[i]
    ost2= 0 if x%34==0 else 34-x%34
    count+=k[ost2]

    ost=x%34
    k[ost]+=1
print(count)