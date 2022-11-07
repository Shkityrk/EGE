from numba import *

@jit()
def f():
    for x in range(1,300):
        for y in range(1,300):
            s='1'*x+'3'*y
            p=s
            while '12' in s or '13' in s:
                s=s.replace('12', '21', 1)
                s=s.replace('31', '23', 1)
                s=s.replace('13', '23', 1)
            if s.count('1')==0:
                if s.count('2')*2+s.count('3')*3==404:
                    print(len(p))
                    pass

f()