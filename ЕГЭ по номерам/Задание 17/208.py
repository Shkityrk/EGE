a=[int(x) for x in open("data/17-205.txt")]
l=[]
for i in range(1,len(a)):
    if (str(a[i-1])[-2:]=='17' or str(a[i])[-2:]=='17') and (abs(a[i-1])+abs(a[i]))%2==0:l.append(a[i]+a[i-1])
print(len(l), max(l))