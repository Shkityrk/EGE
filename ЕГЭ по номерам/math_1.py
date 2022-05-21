def f(x):
    if 6*x**4-7*x**3-36*x**2+7*x+6==0:
        return True
    else:return False
n=1
for x in range(-10000, 10000):
    if f(x): n=n*x
print(n)