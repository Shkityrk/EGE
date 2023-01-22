a=[int(x) for x in open("18-k3.txt")]
k=0

for i in range(len(a)):
    for j in range(9, 100000):
        if i+j<len(a):
            if (a[i]+a[i+j])%2!=+0:k+=1
print(k)