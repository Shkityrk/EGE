# общий вид задачи
for A in range (1, 1000):
    flag=0
    for x in range (1,1000):
        if ( ( (x%12==0) and (x%A==0)) <= ((x%42==0) or (x%12 !=0)) ) ==0:
            flag=1
            break
    if flag == 0:
        print (A)
