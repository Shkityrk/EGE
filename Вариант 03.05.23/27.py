f=open('27_A.txt')


a=[int(x) for x in f.readlines()]
k=a[0]
a=a[2:]
ans=[]
for i in range(len(a)):
    for j in range(i+k,len(a)):
        if a[i]%26==0 or a[j]%26==0:
            if abs(a[i]-a[j])%2!=0:
                ans.append(a[i]+a[j])
print(max(ans))