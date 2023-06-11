f=open('files_compege/test.txt')
n=int(f.readline())
a=[]
k=0
for i in range(n):
    x=int(f.readline())
    for y in a:
        if (x+y)%8!=0:k+=1

    a.append(x)
    if len(a)>7:a.pop(0)
print(k)