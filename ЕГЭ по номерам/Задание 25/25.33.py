
start, end = 194441, 196500
def is_prime(n):
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            return False
    return True

number=0

for i in range(start,end+1):
    if is_prime(i) and i%100==93:
        number+=1
        print(number, i)