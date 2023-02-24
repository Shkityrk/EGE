s=open('data/k7/k7-100.txt').readline()
c=m=0
for i in range(len(s)):
    if s[i]=='C':
        c+=1
        m=max(c,m)
    else: c=0
print(m)