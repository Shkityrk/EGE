f=open('schelchok/5_B__1vjxz.txt')
n=int(f.readline())
s=[0]

for i in range(n):
    tr=[int(x) for x in f.readline().split()]
    p=[tr[0]+tr[1],tr[2]+tr[1],tr[2]+tr[0]]

    s=[a+b for a in s for b in p]
    s={x%6:x for x in sorted(s)}.values()

print(max(x for x in s if x%6==0))