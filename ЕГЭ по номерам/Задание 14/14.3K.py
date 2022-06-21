s=2*27**7+3**10-9
k=0
while s!=0:
    if s%3==0: k+=1
    s//=3
print(k)