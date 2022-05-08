f=open('zadanie24_2.txt')
s=f.readline()
mx=-1
kol = 0
for i in range(len(s)):

    if s[i]=='L' :
        kol+=1
        if kol>mx:
            mx=kol
    else:
        kol=0
print(mx)