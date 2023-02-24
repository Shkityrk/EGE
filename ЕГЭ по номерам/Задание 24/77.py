s=open('data/k8/k8-2.txt').readline()
c=0
m=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        c+=1
        m=max(c,m)
    else:c=1
print(m)
