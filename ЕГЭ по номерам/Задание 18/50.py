a=[int(x) for x in open("18-k3.txt")]
k=0

for i in range(len(a)):
    for j in range(1,4):
        if i+j<len(a): k=max(k, a[i]+a[i+j])
print(k)