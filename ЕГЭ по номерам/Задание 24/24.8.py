f=open ('s1.txt')

kol=0
for s in f:
    countAB=0
    for i in range(1,len(s)):
        if s[i-2]=='A' and s[i]=='B':
            countAB+=1
            if countAB>5:
                kol+=1

print (kol)