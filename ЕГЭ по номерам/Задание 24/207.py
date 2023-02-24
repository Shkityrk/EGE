s=open('data/24-1.txt').readline()
for c in 'QWRTPSDFGHJKLZXCVNM':
    s=s.replace(c,'B')
for c in 'EIOUY':
    s=s.replace(c,'A')
na=0
c=m=0
for i in range(len(s)):
    if s[i] == 'A':
        na += 1
    if na<=5:
        c+=1
        m=max(c,m)
    if na>5:
        c=0
        na=0

print(m)

