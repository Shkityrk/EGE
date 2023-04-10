a=set(range(10000))
p={2,4,6,8,10,12,14,16,18,20}
q={5,10,15,20,25,30,35,40,45,50}

def f(x):
    A=x in a

    P=x in p
    Q=x in q
    return (A<=P) and (Q<=(not A))
for x in range(1,10000):
    if f(x)==0:
        a.remove(x)
print(len(a))