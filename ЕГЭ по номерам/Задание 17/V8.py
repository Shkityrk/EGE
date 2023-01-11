a=[int(x) for x in open("17/17var08.txt")]
l=[]

for i in range(1,len(a)):
    if abs(a[i-1])%5==0 and abs(a[i])%5==0: l.append(a[i-1]+a[i])

print(len(l), min(l))