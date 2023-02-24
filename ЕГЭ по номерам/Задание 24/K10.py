s=open('K/24-10.txt').readline()

c=m=1
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        c+=1
        m=max(c,m)
    else:c=1
print(m)