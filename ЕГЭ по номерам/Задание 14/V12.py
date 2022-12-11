x=3**333+3**22-9**111-8
k=0
while x>0:
    if x%3==2:k+=1
    x=x//3
print(k)
