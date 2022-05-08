f=open("2.txt")
a=[]
for s in f:
    a.append(int(s))

kol=0
mn=200000

for i in range(0, len(a)-1):
    if (abs(a[i])%10==6 and abs(a[i])%3==0 ) or (abs(a[i+1])%10==6 and abs(a[i+1])%3==0 ):
        kol+=1
        if a[i]<mn:
            mn=a[i]
        if a[i+1]<mn:
            mn=a[i+1]
print(kol, mn)