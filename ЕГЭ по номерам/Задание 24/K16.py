s=open('K/24-16.txt').readline()
m=0
s=s.split('A')
for i in range(len(s)-1):
    n=s[i]+'A'+s[i+1]
    m=max(m,len(n))
print(m)