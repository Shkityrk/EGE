for x in range(0,100):
    s1='19'+str(x)+'61'
    s2='3393'+str(x)
    s3='60'+str(x)+'05'
    if int(s1,12)+int(s2,17)==int(s3,15):
        print(int(s3,15))