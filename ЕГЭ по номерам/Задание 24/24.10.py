f=open('k7a-1.txt')
s=f.readline()

max=-1
c=0
for i in range (0, len(s)):
    if s[i]=='A' or s[i]=='B' or s[i]=='C':
        c+=1
        if c>max:
            max=c
    else:
        c=0
print (max)