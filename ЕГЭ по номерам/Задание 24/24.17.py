f=open("j6.txt")
s=f.readline()
c=0
mx=0
for i in range (1,len(s)):
    if s[i-1] < s[i]:
        c+=1
        if c>mx:
            mx=c
    else:
        c=0
print (mx)