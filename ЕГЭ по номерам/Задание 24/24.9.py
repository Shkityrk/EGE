f=open('k7.txt')
s=f.readline()

max=-1
c=0
for i in range (0, len(s)):
    if s[i]=='B':
        c+=1
        if c>max:
            max=c
    else:
        c=0
print (max)