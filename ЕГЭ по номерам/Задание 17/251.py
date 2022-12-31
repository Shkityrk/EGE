a=[int(x) for x in open("data/17-243.txt")]
mx=max(a[i] for i in a if a[i]%153==0)
def f(n):
    s=''
    while n!=0:
        s=str(n%2)+s
        n//=2
    return s
l=[]
for i in range(1,len(a)):
    if (a[i-1]>mx or a[i]>mx) and ('1111' in f(a[i-1]) or '1111' in f(a[i])):l.append(a[i-1]+a[i])
print(len(l), min(l))