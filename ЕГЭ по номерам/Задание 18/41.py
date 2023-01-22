a=[int(x) for x in open("18-k1.txt")]

mx=0
k=0
for i in range(len(a)):
    if a[i]%2==0:
        k+=a[i]
        mx=max(mx,k)
    else:k=0
print(mx)