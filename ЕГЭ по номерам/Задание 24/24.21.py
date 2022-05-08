f=open("24-j5.txt")
s=f.readline()
kol=0

for i in range(6,len(s)):
    if s[i-6]=='S' and s[i-5]=='O' and s[i-4]=='C' and s[i-3]=='K' and s[i-2]=='C' and s[i-1]=='O' and s[i]=='S':
        kol+=1
print(kol)