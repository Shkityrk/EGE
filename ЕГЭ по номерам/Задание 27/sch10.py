f=open('schelchok/27-10b__1vjms.txt')
n=int(f.readline())
s=[0]

for i in range(n):
    p=[int(x) for x in f.readline().split()]
    s=[a+b for a in s for b in p]
    s={x%8:x for x in sorted(s, reverse=True)}.values()

print(min(x for x in s if x%8==0))

