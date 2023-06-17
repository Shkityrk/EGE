s=open('schelchok/6__1vv4p.txt').readline()

ans=0
letter=1

mx=0
k=1
for i in range(1,len(s)):
    if ord(s[i-1])>ord(s[i]):
        k+=1
        if k>=mx:
            mx=k
            ans=letter
    else:
        k=1
        letter =i+1
print(ans)