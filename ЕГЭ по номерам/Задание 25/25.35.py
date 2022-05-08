def f(x):
    if x==1:
        return False
    for j in range (2,int(x**0.5)+1):
        if x%j==0:
            return False
    return True
count=0
mini=1000000
for i in range (378312,446492+1):
    for j in range (2,int(i**0.5)+1):
        if i%j==0 and f(j):
            if j!=(i//j) and f(i//j):
                count+=1
                if i<mini:
                    mini=i
print(count,mini)