from numba import njit

@njit()
def f():
    for a in range(2031065,3_000_000):
        f=1
        for x in range(1, 7000):
            for y in range(1, 7000):
                if 5*x+3*y<=11112:
                    f*=(680*y+256*x<a)
        if f == 1:
            print(a)
            break



if __name__=="__main__":
    f()