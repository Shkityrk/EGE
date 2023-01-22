a=[int(x) for x in open("18-k3.txt")]
k=0
for i in range(len(a)):
    for j in range(1,6):
        if i+j<len(a) and (1000<a[i]+a[i+j]<1500):k+=1
print(k)