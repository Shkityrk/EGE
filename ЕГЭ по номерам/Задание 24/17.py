a=open('data/k7/k7-94.txt').readline()
c=m=0
for i in range(len(a)):
    if a[i]=='C':
        c+=1
        m=max(c,m)
    else: c=0
print(m)