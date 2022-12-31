a=[int(x) for x in open("data/17-5.txt")]
l=[]
for i in range(1,len(a)):
    if abs(a[i-1])%2==0 or abs(a[i])%2==0:
        l.append(a[i-1]+a[i])
print(len(l), max(l))