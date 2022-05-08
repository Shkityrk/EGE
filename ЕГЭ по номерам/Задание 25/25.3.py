from numba import njit

@njit
def a():
    start, end= 3532000,3532160
    for i in range(start,end+1):
        d=0
        for j in range(1,i+1):
            if i%j==0:
                d+=1
        if d==2:
            print(i)
if __name__=="__main__":
    a()