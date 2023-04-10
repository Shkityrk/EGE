a=set()
def f(x):
    A=x in a
    return not((not(A)) and (x in {3,6,9,12})) or (x not in {1,2,3,4,5,6})
for x in range(1,1000):
    if f(x)==0:a.add(x)
print(len(a))