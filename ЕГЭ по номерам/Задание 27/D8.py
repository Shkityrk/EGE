f=open('files_compege/27B_2728.txt')
n=int(f.readline())

a0=[]
a1=[]

for i in range(n):
    x=int(f.readline())
    if x%2==0:a0.append(x)
    else:a1.append(x)

a0.sort()
a1.sort()
b=a0[-1000:]+a1[-1000:]
ans=0
for i in range(len(b)):
    for j in range(i,len(b)):
        if (b[i]+b[j])%2==0 and  (b[i]%23==0 or b[j]%23==0):ans=max(ans,b[i]+b[j])
print(ans)
