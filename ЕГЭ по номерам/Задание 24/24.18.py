with open("j8.txt", "r") as f:
    s=f.readline()
c=1
mx=0
for i in range (1,len(s)):
    if int(s[i-1])+int(s[i])>=10:
        c+=1
        if c>mx:
            mx=c
    else:
        c=1
print(mx)