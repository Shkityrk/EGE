f=open("2 (2).txt")
a=[]
for s in f:
    a.append(int(s))
kol=0
mn=2000000
for i in range(0, len(a)-1):
    if a[i] <a[i+1]:
        kol+=1
        if abs(a[i+1]-a[i]) <mn:
            mn=abs(a[i+1]-a[i])
print(kol, mn)