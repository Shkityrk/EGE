s=open('data/k7/k7c-2.txt').readline()
c=m=0
for i in range(len(s)-2):
    if s[i] in 'ACE' and s[i+1] in 'ADF' and s[i+2] in 'ABF' and s[i]!=s[i+1] and s[i+1]!=s[i+2]:
        c+=1
print(c)