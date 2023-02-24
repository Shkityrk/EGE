s=open('K/24-18.txt').readline()
while 'KOT' in s:s=s.replace('KOT','*')
c=m=0
for i in range(len(s)):
    if s[i]=='*':
        c+=1
        m=max(c,m)
    else:c=0
print(m)