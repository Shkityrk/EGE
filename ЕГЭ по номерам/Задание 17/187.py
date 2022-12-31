a=[int(x) for x in open("data/17-6.txt")]
l=[]
def count(n):
    k=0
    while n!=0:
        if n%2==1:k+=1
        n//=2
    return k
for i in range(2,len(a)):
    if count(a[i-2])==3 and count(a[i-1])==3 and count(a[i])==3:l.append(max(a[i-2],a[i-1],a[i]))
print(len(l), sum(l))