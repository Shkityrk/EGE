def f(n):
    if n<=18: return n+3
    if n>18 and n%3==0: return (n//3)*f(n//3)+n-12
    if n>18 and n%3!=0: return f(n-1)+n*n+5
k=0
for n in range(1,801):
    s=str(f(n))
    if all(l not in s for l in '13579'): k+=1
print(k)