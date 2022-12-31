n=int(input())
for i in range(2,n):
    if 2**(i-1)%i==1:
        print(i)
