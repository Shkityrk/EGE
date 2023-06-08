f=open('kompege/17_1998.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(2,len(a)):
    if abs(a[i-2]*a[i-1]*a[i])%7==0 and abs(a[i-2]+a[i-1]+a[i])%10==5:
        ans.append(a[i-2]+a[i-1]+a[i])
print(len(ans),max(ans))