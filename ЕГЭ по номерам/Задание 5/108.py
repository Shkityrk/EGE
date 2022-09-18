k=0
for i in range(10,101):
    if i%4==3 and i%3==1 and i%2==1:
        k+=1
print(k)