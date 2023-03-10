a=[int(x) for x in open('data/17-328.txt')]

l=[]
nech=[]
for x in a:
    if x%2!=0:nech.append(x)
n=sum(nech)/len(nech)
for i in range(2,len(a)):
    o1=str(oct(a[i-2]+a[i-1]))
    o2=str(oct(a[i-2]+a[i]))
    o3 = str(oct(a[i-1]+a[i]))
    if '7' not in o1 and '7' not in o2 and '7' not in o3 and (a[i-2]+a[i-1]+a[i] )<n:l.append(a[i-2]+a[i-1]+a[i])
print(len(l), max(l))