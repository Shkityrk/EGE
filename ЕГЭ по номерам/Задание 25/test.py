n=100
for i in range(2,n):
        if n%i==0 and 2**(i-1)%i==1:
            print(i)
