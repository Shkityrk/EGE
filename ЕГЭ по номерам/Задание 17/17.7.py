f=open("5.txt")
a=[]
for s in f:
    a.append(int(s))
kol=0
mn=min(a)
poz=1
for i in range(1, len(a)):
    if a[i]==mn:
        kol+=1
        poz=i
print(kol, poz+1)