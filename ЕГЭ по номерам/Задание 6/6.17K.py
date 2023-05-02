k=0
for x in range(0,200):
    for y in range(0,30):
        if y>0 and y<15 and y<3*x and y>(x//4)-14:k+=1
print(k)