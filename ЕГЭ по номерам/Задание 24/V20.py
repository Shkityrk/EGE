s=open('24/24var14-20.txt').readline()
c=m=0
for i in range(len(s)):
    if s[i] in '13579':
        c+=1
        m=max(c,m)
    else:c=0
print(m)