s=open('24/24var04.txt').readline()
'''l=0
m=0
nab=0
for i in range(len(s)-1):
    if s[i]+s[i+1]=='AB':
        l+=2
        nab+=1
    else: l+=1
    if nab==22:
        m=max(m,l)
        nab=0
        l=0
print(m)


'''
s=s.replace('BA','AB')
s=s.split('AB')

m=0
for i in range(len(s)-21):
    l='AB'*21
    for x in range(21):
        l+=s[i+x]
    m=max(len(l),m)
print(m)

