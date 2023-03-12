a=[int(x) for x in open('files/17_6752.txt')]
n=sum(1 for i in range(len(a)) if a[i]%3==0)
print(n)
r=[]

for i in range(1,len(a)):
    if (a[i-1]<0 or a[i]< 0) and a[i-1]+a[i]<n:r.append(a[i-1]+a[i])

print(len(r),max(r))
