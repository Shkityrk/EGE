f=open('schelchok/1-3__1vq2c.txt')
s=[str(x) for x in f.readlines()]
k=0

for i in s:
    if i.count('N')<i.count('B'):k+=1
print(k)