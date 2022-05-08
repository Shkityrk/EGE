f=open("j7.txt")
s=f.readline()
c=1
mx=0
for i in range (1, len(s)):
    if int(s[i-1])%2==int(s[i])%2:
        c+=1
        if c>mx:
            mx=c
    else:
        c=1
print (mx)
