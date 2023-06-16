f=open('schelchok/4__1vq2f.txt')
s=[str(x) for x in f.readlines()]
k=0
for  i in s:
    if i.count('R')>64:
        print(i)

