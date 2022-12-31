a=[int(x) for x in open("data/17-202.txt")]
l=[]

for i in range(2,len(a)):
    if a[i-1]>0 and len(str(a[i-1]))==3 and a[i-1]%10==5:l.append(a[i-2]+a[i-1]+a[i])
print(len(l), max(l))