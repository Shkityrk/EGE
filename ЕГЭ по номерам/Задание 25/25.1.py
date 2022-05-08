start = 180201
end = 180260

for x in range(start, end+1):
    count_d = 0
    div = []
    for d in range(1,x+1):
        if x% d ==0:
            count_d +=1
            div.append(d)
        if count_d>4:
            break
    if count_d ==4:
        if div[3]%2==0 or div [2]%2==0:
            print (div[3], div [2], end= ' ')