s=open('data/k8/k8-4.txt').readline()

m=0
c=0
char=s[0]
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c+=1
        if c>m:
            m=max(c,m)
            char=s[i]
    else: c=1
print(char, m)
