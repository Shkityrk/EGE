def f(x,y,a):
    return (2*x+y!=70) or (x<y) or (a<x)
m=-1000
for a in range(1,1000):
    if all(f(x,y,a) for x in range(1,1000) for y in range(1,1000)):
        m=max(m,a)
print(m)