f=open('data/17__1sso9.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
k=0
for i in range(len(a)):
    for j in range(i+3,len(a)):
        if (a[i]*a[j])%34==0:k+=1
print(k)