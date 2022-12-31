a=[int(x) for x in open("data/17-4.txt")]
l=[]
for i in range(len(a)):
    if a[i]%5==3 and a[i]%9==5 and a[i]%8!=7:l.append(a[i])
print(len(l), max(l))