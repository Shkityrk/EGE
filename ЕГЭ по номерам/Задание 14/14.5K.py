
for x in range(5,2000):
    s=125**200-5**x+74
    c=0
    while s!=0:
        if s%5==4: c+=1
        s=s//5
    if c==100:
       print(x)

