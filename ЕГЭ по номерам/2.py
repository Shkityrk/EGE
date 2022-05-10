def num_d(x):
    s=str(x)
    if len(s)>5: return False
    else: return True
def f(n, o):
    s=[]
    while n != 0:
        s. append(n % o)
        n = n // o
    s=reversed(s)
    l=int(''.join(map(str, s)))
    return l

q,b = map(int, input().split())
flg=0
for p in range(1,q,1):
    dr=p/q
    if b==10:
        if num_d(dr):
            print(p)
            flg+=1
            break
    else:
        p1=f(p,b)
        q1=f(q,b)
        dr=p1/q1

        if num_d(dr):
            print(p)
            flg+=1
            break

if flg ==0: print('-1')

