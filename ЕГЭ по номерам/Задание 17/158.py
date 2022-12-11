with open("data/17-2.txt") as f:
    a=[int(x) for x in f.readlines()]
k=0
kol=0
mx_len=0
for i in range(1,len(a)):
    if a[i-1]>a[i]:
        k+=1
    else:
        mx_len=max(mx_len,k)
        k=0

for i in range(1,len(a)):
    if a[i-1]>a[i]:
        k+=1
        if k==mx_len:
            kol+=1
    else:k=0
print(mx_len,kol)