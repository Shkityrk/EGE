def is_true(n):
    for de in range(2, n//2+1):
        d=de**2
        if n % d ==0:
            return False
    return True

su=0
for i in range(2945, 18295):
    if is_true(i):
        su+=i
print(su)
