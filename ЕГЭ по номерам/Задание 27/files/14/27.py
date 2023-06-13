f=open('27-14b.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
ans=0
s=[0]*12


for i in range(n):
    x=a[i]
    ost=x%12

    ost2=0 if x%12==0 else 12-x%12
    ans+=s[ost2]
    s[ost]+=1
print(ans)
