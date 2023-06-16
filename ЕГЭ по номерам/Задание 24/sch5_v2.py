f=open('schelchok/1-3__1vq2c.txt')
s=[str(x) for x in f.readlines()]
k=0
letter=''
ans=0
for i in s:
    kol=1
    for j in range(1,len(i)):
        if i[j-1]==i[j]:
            kol+=1
            if kol>=k:
                k=max(kol,k)
                letter=i[j]
        else:kol=1

for i in s:
    ans+=i.count(letter+'U')
print(letter,ans)

