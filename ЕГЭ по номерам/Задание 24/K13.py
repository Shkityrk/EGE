s=open('K/24-13.txt').readline()
c=''
m=1
index=''
for i in range(len(s)-1):
    if s[i]>s[i+1]:
        c+=s[i]
        if len(c)>m:
            m=len(c)
            index=c
    else:c=''
print(index)