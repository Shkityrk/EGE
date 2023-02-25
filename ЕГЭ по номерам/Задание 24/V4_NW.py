s=open('24/24var04.txt').readline()
s=s.split('AB')
m=0
for i in range(len(s)-21):
    l='AB'*21
    for x in range(21):
        l+=s[i+x]
    m=max(len(l),m)
print(m)