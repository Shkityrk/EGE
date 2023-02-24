s=open('data/24-j8.txt').readline()[:-1]
c=m=1
for i in range(len(s)-1):
    if int(s[i])+int(s[i+1])>=10:
        c+=1
        m=max(c,m)
    else:c=1
print(m)