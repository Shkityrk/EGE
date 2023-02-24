s=open('data/24-1.txt').readline()
c=m=1

for i in range(len(s)-1):
    if s[i+1]>s[i]:
        c+=1
        m=max(c,m)
    else:c=1
print(m)