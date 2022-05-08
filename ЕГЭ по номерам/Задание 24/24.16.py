f=open("157.txt")
s=f.readline()
c=0
mx=0
for i in range(0,len(s)):
    if s[i]!='P' and s[i]!='R':
        c+=1
        if c>mx:
            mx=c
    else:
        c=0

print (mx)