a=[int(x) for x in open("17/17var04.txt")]
l=[]
mx=max(a)

for i in range(2,len(a)):
    if a[i-2]%10!=3 and a[i-1]%10!=3 and a[i]%10!=3 and \
        (a[i-2]**2+a[i-1]**2+a[i]**2)>mx:
        l.append(a[i-2]**2+a[i-1]**2+a[i]**2)
print(len(l), min(l))