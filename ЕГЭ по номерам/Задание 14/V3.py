x=243**540-6*9**530+21*3**511-3*3**70-200
k=0
while x!=0:
    if x%9==8:k+=1
    x//=9
print(k)