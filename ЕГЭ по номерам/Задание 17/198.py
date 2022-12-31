a=[int(x) for x in open("data/17-10.txt")]
l=[]

def f(n):
    s=[]
    while n!=0:
        s.append(n%7)
        n//=7
    s.reverse()
    return s

for i in range(1,len(a)):
    r=f(a[i-1]+a[i])
    for x in range(0, int(len(r) ** 0.5)):
        if r[x] == r[len(r) - 1 - x]:l.append(sum(r))

print(len(l), max(l))

