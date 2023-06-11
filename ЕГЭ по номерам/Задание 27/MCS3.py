f=open('files_compege/27-A_814.txt')
n=int(f.readline())
s=[0]

for i in range(n):
    p=[int(x) for x in f.readline().split()]
    s=[a+b for a in s for b in p]
    s={x%5:x for x in sorted(s, reverse=True)}.values()
print(min(x for x in s if x%5!=0))