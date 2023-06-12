f=open('schelchok/test11.txt')
n=int(f.readline())
ans=-10**20
a=[int(x) for x in f.readlines()]

s=[-10**20]*6

for i in range(n):
    ost=a[i]%6
    s[ost]=max(s[ost], a[i])

for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            for l in range(len(s)):
                if s[i]!=s[j]!=s[k]!=s[l]:
                    if (s[i]+s[j]+s[k]+s[l])%6==0:
                        ans=max(ans,(s[i]+s[j]+s[k]+s[l]) )
                        print(ans,s[i],s[j],s[k],s[l])
print(ans)