s=open('data/k8/k8-9.txt').readline()
c=m=1
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        c+=1
        if c>m:m=c
    else: c=1
print(m)