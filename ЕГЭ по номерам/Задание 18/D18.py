a=[int(x) for x in open("n18.txt")]
k=0
for i in range(len(a)):

    for j in range(1050):
        s = a[i]
        if i+j<len(a) and j-i>=9:
            s+=a[i+j]
        if s%2!=0:
            k+=1
print(k)