s=open('schelchok/7__1vv4q.txt').readline()

kol=0
k=2

for i in range(2,len(s)):
    if s[i-2]!=s[i-1] and s[i-1]!=s[i] and s[i-2]!=s[i]:k+=1
    else:
        kol=max(kol,k)
        k=2
print(kol)