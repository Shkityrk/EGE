k=0
mx=1
for x in range(2461,9720):
    if 3<=(x//10%10)<=7 and x//100%10!=1 and \
       x//100%10!=9:
        k+=1
        mx=max(mx,x)
print(k,mx)
