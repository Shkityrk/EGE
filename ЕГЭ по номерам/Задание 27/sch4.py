f=open('schelchok/27-4b__1vjmg.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]

k13_0=k13_1=k_0=k_1=0
count=0
for i in range(n):
    x=a[i]
    if x%13==0 and x%2==0:k13_0+=1
    if x % 13 == 0 and x % 2 != 0: k13_1 += 1
    if x % 13 != 0 and x % 2 == 0: k_0 += 1
    if x % 13 != 0 and x % 2 != 0: k_1 += 1

countB= k13_0*k13_1 + k13_0*k_1 + k13_1*k_0

print(countB)