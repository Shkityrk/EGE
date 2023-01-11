a=[int(x) for x in open("17/17var07.txt")]
l=[]

for i in range(1,len(a)):
    if abs(a[i-1])%3==0 and abs(a[i])%3==0:l.append(a[i-1]+a[i])
print(len(l), max(l))