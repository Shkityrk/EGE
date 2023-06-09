f=open('course/1.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
k=0
for i in range(n):
    for j in range(i+1,n):
        if abs(a[i]-a[j])%13==0 and (a[i]*a[j])%2==0:
            k+=1
print(k)