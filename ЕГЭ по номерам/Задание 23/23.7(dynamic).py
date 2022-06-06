a=[0]*100
a[22]=1
for i in range(22,2,-1):
    if i-1>=2: a[i-1]+=a[i]
    if i - 3 >= 2: a[i - 3] += a[i]
    if i // 3 >= 2: a[i // 3] += a[i]
print(a[2])