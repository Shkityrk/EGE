a=[int(x) for x in open("18-k3.txt")]
k=0

for i in range(len(a)):
    for j in range(11, 10000):
        if i+j<len(a) and (a[i]+a[i+j])<200:k+=1
print(k)