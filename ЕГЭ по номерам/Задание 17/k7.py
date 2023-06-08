f=open('kompege/17_1994.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(1,len(a)):
    if a[i-1]*a[i]>0 and (a[i-1]+a[i])%7==0:ans.append(a[i-1]*a[i])
print(len(ans), min(ans))