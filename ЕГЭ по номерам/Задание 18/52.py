a=[int(x) for x in open("18-k3.txt")]
k=1
mx_len=0
for i in range(1, len(a)):
    if a[i-1]<a[i]:
        k+=1
        mx_len=max(k,mx_len)
    else:k=1
print(mx_len)