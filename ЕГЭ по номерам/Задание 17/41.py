k=0
mx=1

for x in range(2371, 9433):
    if x%64==13 or x%64==15 and \
       x%3!=0 and x%5!=0:
        k+=1
        mx=max(mx,x)
print(k,mx)
