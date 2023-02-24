s=open('data/24-215.txt').readline()
s=s.replace('B','A').replace('C','A').replace('2','1').replace('3','1')
s=s.replace('A1A1A','A1A A1A')
while 'A1A' in s:s=s.replace('A1A','*')
c=m=0
for i in range(len(s)):
    if s[i]=='*':
        c+=1
        m=max(c,m)
    else:c=0
print(m)