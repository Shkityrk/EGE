f=open("s1.txt")
s=f.readline()
kol=0
for s in f:
    if s.count('C')>s.count('O'):
        kol+=1
print(kol)