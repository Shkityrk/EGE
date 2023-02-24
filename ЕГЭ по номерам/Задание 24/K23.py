s=open('K/24-23.txt').readline()

c=m=1
for i in range(len(s)-2):
    if s[i]+s[i+2]=='AA' or s[i]+s[i+2]=='CC':
        c+=1
        m=max(c,m)
    else:c=1
print(m)
