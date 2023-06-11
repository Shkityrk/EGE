f=open('files_compege/27B_2727.txt')
n=int(f.readline())

a31=[]
a=[]
for i in range(n):
    x=int(f.readline())
    if x%31==0:a31.append(x)
    else:a.append(x)
a31.sort()
a.sort()
a31=a31[:10]
a=a[:10]
r=int(a31[0])*int(a31[1])
r1=int(a31[0])*int(a[0])
print(min(r,r1))