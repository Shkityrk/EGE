s=open('K/24-24.txt').readline()
while 'CA' in s:s=s.replace('CA','*')
print(s)
c=m=0
for i in range(len(s)):
    if s[i]=='*':
        c+=1
        m=max(c,m)
    else:c=0
print(m*2)