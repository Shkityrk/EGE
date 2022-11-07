from numba import njit
@njit()
def f():
    print('begin')
    mx=-100
    a=['13','31', '11','33']
    for n1 in range(0,500):
        for n2 in range(0,500):
            for a1 in range(len(a)):
                for a2 in range(len(a)):
                    s=a[a1]*n1+a[a2]*n2
                    p=s
                    if s.count('1')==0 or s.count('3')==0:
                        pass
                    while '12' in s or '13' in s:
                        s=s.replace('12', '21', 1)
                        s=s.replace('31', '23', 1)
                        s=s.replace('13', '23', 1)
                    if s.count('1')==0:
                        if s.count('2')*2+s.count('3')*3==404:
                            mx=max(len(p), mx)
                            print(mx)
    print(mx)

f()