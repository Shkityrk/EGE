f=open("6.txt")
a=[]
for s in f:
    a.append(s)
mx=0
for i in range(0,len(a)-1):
    n=0
    if a[i]>a[i+1]:
        n+=1
        if n>mx:
            mx=n
    else:
        n=0
for i in range(0,len(a)-1):
    for j in range(mx):
