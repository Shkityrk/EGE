k=0
mx=100
for x in range(1012, 9639):
    if x%3==0 and x%11!=0 and x%13!=0 and x%17!=0 and x%19!=0:
        k+=1
        mx=max(x,mx)
print(k, mx)
