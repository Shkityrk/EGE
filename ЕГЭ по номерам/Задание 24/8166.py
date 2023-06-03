s=open('data/24_8166.txt').readline()
ans=0
k=1
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        k+=1
        ans=max(ans,k)
    else:k=1
print(ans)