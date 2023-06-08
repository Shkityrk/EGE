f=open('kompege/17_1999.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(2,len(a)):
    if all(abs(a[i-x])%3==0 for x in range(3)) and any(abs(a[i-x])%12==0 for x in range(3)):
        ans.append((a[i-2]+a[i-1]+a[i])//3)
print(len(ans),min(ans))