a=[int(x) for x in open("data/17-300.txt")]
l=[]

mx=max(m for m in a if m%401==0)

def su(n):
    s=0
    n=abs(n)
    while n!=0:
        s+=n%10
        n//=10
    return s

for i in range(2,len(a)):
    s1=su(a[i-2])
    s2=su(a[i-1])
    s3=su(a[i])
    if (a[i-2]+a[i-1]+a[i])>mx:
        if a[i-2]%(s2+s3)==0 or a[i-1]%(s1+s3)==0 or a[i]%(s1+s2)==0:
            l.append((a[i-2]+a[i-1]+a[i]))
print(len(l), min(l))