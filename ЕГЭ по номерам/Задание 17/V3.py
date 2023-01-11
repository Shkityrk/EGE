a=[int(x) for x in open("17/17var03.txt")]
l=[]
mx=max(a)
for i in range(2,len(a)):
    k=0
    for x in range(3):
        if a[i-x]%10==0:k+=1
    if k==1 and (a[i-2]+ a[i-1]+ a[i])<mx:
        l.append(a[i-2]+ a[i-1]+ a[i])

print(len(l), max(l))