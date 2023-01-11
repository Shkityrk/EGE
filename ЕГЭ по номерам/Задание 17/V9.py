a=[int(x) for x in open("17/17var09.txt")]
l=[]

for i in range(1, len(a)):
    if abs(a[i-1])%10==5 and abs(a[i])%10==5: l.append(abs(a[i-1]-a[i]))
print(len(l), max(l))