k=0
n=81**100-3**200-3**50+2
while n!=0:
    if n%3==2:k+=1
    n=n//3
print(k)