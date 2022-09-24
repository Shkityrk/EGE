k=0
for n in range(1,100000):
    r=n
    r=r//3 if r%3==0 else r-1
    r=r//5 if r%5==0 else r-1
    r=r//11 if r%11==0 else r-1
    if r==8:
        print(n)
