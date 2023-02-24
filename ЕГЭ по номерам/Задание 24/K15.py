s=open('K/24-15.txt').readline()
sub=0
m=1000000
for i in range(len(s)):
    if s[i]=='D':
        sub+=1
    elif sub!=0:
        m=min(m,sub)
        sub=0
print(m)