n=49**129+7**131-2
s=[]
while n!=0:
    s.append(n%7)
    n//=7
m=max(s)
for i in range(len(s)):
    if s[i]==0:s[i]=m
print(s.count(m))