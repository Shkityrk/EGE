from numba import njit

@njit
def a():
    start,end = 266868, 336868

    def is_prime(n):
        for b in range(2,int(n**0.5)+1):
            if n%b==0:
                return 0
        return 1
    kol=0
    mx=-100
    for i in range(start,end+1):
        for div1 in range(1,int(i**0.5)+1):
            if is_prime(div1):
                for div2 in range(1, int(i ** 0.5) + 1):
                    if is_prime(div2):
                        if div1!=div2:
                            if div1 * div2 == i:
                                kol += 1
                                if i > mx:
                                    mx = i


    print(kol,mx)


a()
