f=open("2 (1).txt")
a=[]
for s in f:
    a.append(int(s))

kol=0
mx=-200015

for i in range(0,len(a)-1):
    if (a[i]%9==0 and abs(a[i])%8==3 ) or (a[i+1]%9==0 and abs(a[i+1])%8==3 ):
        kol+=1
        if a[i]>mx:
            mx=a[i]
        if a[i+1]>mx:
            mx=a[i+1]
print(kol, mx)

# привет


print('привет')