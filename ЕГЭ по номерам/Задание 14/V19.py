x=3**2017+9**1000-27
k=0
while x!=0:
    if x%3==2:k+=1
    x//=3
print(k)