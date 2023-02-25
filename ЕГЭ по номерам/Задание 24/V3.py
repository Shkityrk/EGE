s=open('24/24var03.txt').readline()
s=s.split('AB')
mn=10**10
for i in range(len(s)-21):
    l='AB'*21
    for x in range(21):
        l+=s[i+x]
    if len(l)<mn:
        mn=len(l)
print(mn)