def f(n):
    if n<10: return n
    if n>=10: return f(g(n))
def g(n):
    if n<10: return n
    if n>=10: return n%10+g(n//10)
print(f(12345678987654321))