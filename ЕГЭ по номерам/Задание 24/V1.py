s=open('24/24var01.txt').readline()

for c in 'CDE':
    s=s.replace(c,'B')
s=s.split('A')
m=0
l=''
for i in range(len(s)-3):
    l=s[i]+'A'+s[i+1]+'A'+s[i+2]+'A'+s[i+3]
    if len(l)>m:
        m=len(l)
    l=''
print(m)