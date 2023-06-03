s=open('data/24_7891.txt').readline()
ans=0

for i in range(len(s)):
    for j in range(i+1,len(s)):
        a=s[i:j]
        if a[0]==a[-1] and a.count(a[0])==2:ans=max(len(a),ans)
print(ans)