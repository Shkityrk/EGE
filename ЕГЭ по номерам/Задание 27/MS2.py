f=open('files_compege/27-B_637.txt')
n=int(f.readline())
s=[0]

for i in range(n):
    p=[int(x) for x in f.readline().split()]
    s=[a+b for a in s for b in p]
    s={x%10:x for x in sorted(s)}.values()
print(max(x for x in s if x%10!=5))