s=open('data/24_7853.txt').readline()
s=s.replace('N','*').replace('O','*').replace('T','*')
ans=0
k=2
for i in range(2,len(s)):
    if not(s[i-2]=='*' and s[i]=='*'):
        k+=1
        ans=max(ans,k)
    else:k=2
print(ans)