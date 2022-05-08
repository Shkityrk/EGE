f=open('j5-1.txt')
s=f.readline()
a=0

for i in range(2, len(s)):
    if s[i-2]=='K' and s[i-1]=='C' and  s[i]=='C' :
        if (s[i+1]=='T' and s[i+2]=='T'):
            a==a
        else:
            a +=1
print (a)
