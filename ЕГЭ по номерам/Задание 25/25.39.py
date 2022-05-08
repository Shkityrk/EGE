start ,end = 2 , 3577000
def is_prime (n):
    for d in range(2,int(n**0.5)+1):
        if n%d==0: return False
    return True
num = 0
for i in range(start,end+1):
    if is_prime(i):
        num+=1
print(num)