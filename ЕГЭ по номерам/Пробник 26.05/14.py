n=9**7+3**21-9
c=0
while n!=0:
    if (n%3)==2:
        c+=1
    n=n//3
print(c)