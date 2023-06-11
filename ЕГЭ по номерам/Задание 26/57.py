f=open('data/26-57.txt')
n,m=map(int,f.readline().split())

a=[int(x) for x in f.readlines()]
a.sort(reverse=True)

c=[]
while sum(c)+a[0]<=n:
    c.append()