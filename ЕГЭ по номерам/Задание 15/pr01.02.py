for a in range(1,10000):
    if all((x%a==0) or (x%23==0)<= (x<50 or x>70) for x in range(1,100000)):
        print(a)
