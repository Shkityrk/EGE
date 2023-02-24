s=open('data/24-5.txt').readline()
s=s.replace('()','*')
c=m=0
for i in range(len(s)-1):
    if s[i]=='*':
        c+=1
        m=max(c,m)
    else:c=0
print(m)