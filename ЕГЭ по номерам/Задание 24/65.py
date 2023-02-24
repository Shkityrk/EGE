s=open('data/k8/k8-80.txt').readline()
c=0
m=0
char=''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
        if c>m:
            m=c
            char=s[i]
    else:c=1
print(char, m)