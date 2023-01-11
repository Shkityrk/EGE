a=[int(x) for x in open("17/17var02.txt")]
mx=max(i for i in a if i%2==0)

l=[]

for i in range(1,len(a)):
    if a[i-1]+a[i]==mx:l.append(a[i-1]**2+a[i])
print(len(l), max(l))