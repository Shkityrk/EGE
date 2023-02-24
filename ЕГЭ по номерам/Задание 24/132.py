s=open('data/24-j1.txt').readline()
s=s.replace('КОТ', '*')
c=m=0
for i in range(len(s)):
    if s[i]=='*':
        c+=1
        m=max(c,m)
    else:c=0
print(m)