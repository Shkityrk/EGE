a=[int(x) for x in open("17/17var14.txt")]
l=[]
for i in range(1, len(a)):
    if a[i-1]+a[i]>50 and a[i-1]>0 and a[i]>0:l.append(a[i]*a[i-1])
print(len(l), min(l))