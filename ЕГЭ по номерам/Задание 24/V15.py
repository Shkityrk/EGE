s=open('24/24var14-20.txt').readline()
c=m=1
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        c+=1
        m=max(c,m)
    else:c=1
print(m)