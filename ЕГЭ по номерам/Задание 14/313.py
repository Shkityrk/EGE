def a(n):
    k=0
    while n!=0:
        k+=1
        n//=16
    if k<=8:return True
    else: return False

def b(n):
    k = 0
    while n != 0:
        k += 1
        n//=8
    if k>=11:return True
    else: return False
k=0
for n in range(2,1000000):
    if a(n) and b(n) :
        k+=1
        print(n)
print(k)