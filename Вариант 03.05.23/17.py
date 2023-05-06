a=[int (x) for x in open('17.txt').readlines()]
mx=0
k=[]
for i in range(len(a)):
    if len(str(a[i]))==3:mx=max(mx,a[i])

for i in range(len(a)-1):
    s1=str(a[i])
    s2=str(a[i+1])
    if (len(s1)==3 and len(s2)!=3) or (len(s1)!=3 and len(s2)==3):
        if a[i]+a[i+1]<=mx:k.append(a[i]+a[i+1])
print(len(k),max(k))