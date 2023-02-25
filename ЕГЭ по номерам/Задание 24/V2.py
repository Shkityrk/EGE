s=open('24/24var02.txt').readline()
s=s.split('A')

mn=10**10
for i in range(len(s)-35):
    l = 'A'*35
    for x in range(34):
        l+=s[i+x]
    if len(l)<mn:
        mn=len(l)

print(mn)