s=open('K/24-6.txt').readline()
c=m=0
for i in range(len(s)):
    if s[i] in '1234567890':
        c+=1
        m=max(c,m)
    else:c=0
print(m)