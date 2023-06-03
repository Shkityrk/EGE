f=open('files_compege/27B_2256.txt')
n=int(f.readline())
m=[10**23]*3
ms=0
s,k=0,0
for i in range(n):
    x=int(f.readline())
    s+=x
    if x%5==0:k+=1
    if k%3==0:ms=max(ms,s)
    ms=max(ms,s-m[k%3])
    m[k%3]=min(m[k%3],s)
print(ms)