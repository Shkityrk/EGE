start, end = 2, 20_000
def is_true(n):
    s=[]
    for d in range(1, n//2+1):
        if n%d==0:
            s.append(d)
    if sum(s)>n:
        return True
    else:
        return False
number=0
for i in range(start,end+1):
    if is_true(i):
        number+=1
print(number)