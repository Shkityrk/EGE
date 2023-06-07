def f(x,y,a):
    return ((y*y<=a)<=(y<=10)) and ((x<=9)<=(x*x<a))

for a in range(1,1000):
    if all(f(x,y,a) for x in range(1,10000) for y in range(1,10000)):
        print(a)
        break