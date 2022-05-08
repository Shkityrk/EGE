# Автор: Н. Плотицын

def prime(x):
    sq = int(x**0.5)
    for i in range(2,sq+1):
        if x%i==0:
            return False
    return x>1

k = 0
p1 = 2
for x in range(3,1000001):
    if not prime(x):
        k+=1
    else:
        if k>=90: print(p1, x)
        p1 = x
        k = 0
