a=[int(x) for x in open('data/17-336.txt')]
m=10**10
for i in range(len(a)):
    if a[i]%8==0 and a[i]!=8:
        m=min(m,a[i])

print(m)
l=[]
for i in range(1,len(a)):
    if a[i-1]%m==0 and a[i]%m==0:l.append(max(a[i-1],a[i]))
print(len(l), min(l))