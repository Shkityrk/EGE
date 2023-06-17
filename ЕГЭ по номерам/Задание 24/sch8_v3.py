s=open('schelchok/8__1vv4r.txt').readline()
k=1
kol=0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        k+=1
        kol=max(kol,k)
    else:k=1

print(kol)
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        k+=1
        if k==kol:print(s[i])
    else:k=1


