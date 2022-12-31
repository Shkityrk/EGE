a=[int(x) for x in open("17/17var20.txt")]
l=[]

for i in range(1,len(a)):
    if abs(a[i-1])+abs(a[i])<=200 and abs(a[i-1])+abs(a[i])>=50:l.append(min(a[i-1], a[i]))
print(len(l), min(l))