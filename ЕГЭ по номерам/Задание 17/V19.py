a=[int(x) for x in open("17/17var19.txt")]
l=[]

for i in range(1,len(a)):
    if abs(a[i-1])+abs(a[i])<=700 and abs(a[i-1])+abs(a[i])>=100:l.append(max(a[i], a[i-1]))
print(len(l), max(l))