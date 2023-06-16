f=open('schelchok/1-3__1vq2c.txt')
s=[str(x) for x in f.readlines()]
k=0
for i in s:
    for j in range(4,len(i)):
        if i[j-3]=='T' and i[j]=='O':
            k+=1
            break
print(k)
print(len(s))