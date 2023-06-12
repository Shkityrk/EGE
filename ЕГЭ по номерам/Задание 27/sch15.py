f=open('schelchok/27-15b__1vjn2.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]

k26=k13=k2=0

for i in range(n):
    x=a[i]
    if x%26==0:k26+=1
    elif x%13==0:k13+=1
    elif x%2==0:k2+=1
print(k26*(k26-1)//2 + k26 *(n-k26) + k13*k2)