s=open('data/24-5.txt').readline()
c=m=0

for i in range(len(s)):
    if s[i]=='(':
        c+=1
        m=max(c,m)
    else: c=0
print(m)