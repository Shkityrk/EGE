f=open("4.txt")
a=[]
for s in f:
    a.append(int(s))
mx=max(a)
kol=0
poz1=0
for i in range(1,len(a)):
    if a[i]==mx:
        kol+=1
        if kol==1:
            poz1=i
print(kol, poz1+1)
