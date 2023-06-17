s=open('schelchok/9__1vv4s.txt').readline()

for x in '1234567890':
    while str(x+x) in s:
        s=s.replace(x+x,x)
ans=0
for i in range(len(s)):
    ans+=int(s[i])
print(ans)