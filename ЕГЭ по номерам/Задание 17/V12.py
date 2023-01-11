a=[int(x) for x in open("17/17var12.txt")]
l=[]
n='13579'
for i in range(1,len(a)):
    if str(a[i-1])[-1] in n and str(a[i])[-1] in n and str(a[i-1])[-1]!=str(a[i])[-1]:
        l.append(abs(a[i-1])*abs(a[i]))
print(len(l), min(l))