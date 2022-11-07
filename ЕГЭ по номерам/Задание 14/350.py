for x in range(0,10000):
    s1='3364'+str(x)
    s2=str(x)+'7946'
    s3='55'+str(x)+'87'
    if int(s1,11)+int(s2,12)==int(s3,14):
        print(int(s3,14))
