a=[int(x) for x in open("17/17var01.txt")]
l=[]
mx=max(a)
for i in range(1,len(a)):
    if a[i-1]+a[i]==mx:
        l.append(a[i-1]**2+a[i]**2)
print(len(l), max(l))