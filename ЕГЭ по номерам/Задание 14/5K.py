for x in range(1,1000):
    n=125**200-5**x+74
    k=0
    while n!=0:
        if n%5==4:k+=1
        n//=5
    if k==100:
        print(x)
        break