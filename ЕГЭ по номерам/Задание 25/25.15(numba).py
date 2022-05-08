from numba import njit
@njit

def a():
    st,end=int(652938**0.5), int((1744328+1)**0.5)
    for n in range(st,end+1):
        i=n**2
        a=[]
        for d in range(1,i+1):
            if i%d==0:
                a.append(d)
        if len(a)==5:
            print(a)

a()