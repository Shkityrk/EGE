s=open('K/24-17.txt').readline()
m=0
s=s.split('D')
for i in range(len(s)-2):
    n=s[i-2]+'D'+s[i-1]+'D'+s[i]
    m=max(m,len(n))
print(m)