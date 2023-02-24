s=open('data/24-222.txt').readline()
s=s.split('A')
m=0
for i in range(1,len(s)-3):
    if s[i]==s[i+1]==s[i+2]:
        m=max(m,len('A'+s[i]+'A'+s[i+1]+'A'+s[i+2]+'A'))
print(m)