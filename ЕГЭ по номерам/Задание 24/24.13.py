f=open("k7a-4.txt")
s=f.readline()
mx=0
c=1
for i in range (0,len(s)):
    if s[i]!='D':
        c+=1
        if c>mx:
            mx=c
    else:
        c=1
print (mx)