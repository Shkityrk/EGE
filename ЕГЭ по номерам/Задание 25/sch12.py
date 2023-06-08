def pr(n):
    f=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return 0
    return 1

for n in range(2410000,2410100+1):
    if pr(n):
        print(n)