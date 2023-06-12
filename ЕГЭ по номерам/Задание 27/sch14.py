f=open('schelchok/27-14b__1vjn0.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
k11=k22=k2=0

for i in range(n):
    x=a[i]
    if x%22==0:k22+=1
    elif x%11==0:k11+=1
    elif x%2==0:k2+=1

print( k22*(k22-1)//2 + k22*(n-k22) +k11*k2 )
