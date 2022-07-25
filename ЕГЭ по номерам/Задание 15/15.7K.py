def f(x,a):
    return (((x&13!=0) or (x&a!=0)) <= (x&13!=0)) or ((x%a!=0) and (x%39==0))
m=-100
for a in range(1,1000):
    if all(f(x,a) for x in range(1,10000)):
        m=max(m,a)
print(m)