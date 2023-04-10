a=set()
def f(x):
    A=x in a
    B=x in {1,3,5,7,9,11}
    C=x in {3,6,9,12}
    return B<=(not C) or A
for x in range(1,1000):
    if f(x)==0:
        a.add(x)
print(sum(a))