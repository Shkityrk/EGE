f=open("k7a-6.txt")
s=f.readline()
c=0
mx=0
for i in range(0, len(s)):
    if s[i]=='B' or s[i]=='C' or s[i]=='D' or s[i]=='F':
        c+=1
        if c>mx:
            mx=c
    else:
        c=0
print (mx)