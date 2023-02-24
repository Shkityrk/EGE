s=open('data/24-3.txt').readline()
c=m=1
temp=0
n=0
for i in range(len(s)-1):
    if c==1:
        temp = i
    if s[i]<s[i+1]:
        c+=1
        if c>m:
            m=max(c,m)
            n=temp+1
    else:c=1
print(n)