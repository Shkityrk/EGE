s=open('data/24-1.txt').readline()
c=''
m=0
for i in range(len(s)-1):
    if s[i] in '1234567890':
        c+=s[i]
        m=max(m,int(c))
    else: c=''
print(m)