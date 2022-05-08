
def a():
    start, end = 2, 10_000_000

    def prime_divs(n):
        s=[]
        for d in range(1,n//2+1):
            if n%d==0 :
                flag=True
                for d in range(2, int(n ** 0.5) + 1):
                    if n % d == 0:
                        flag=False
                        break
                if flag:
                    s.append(d)
        return sorted(s)

    mx=0

    for i in range(start,end+1):
        s=prime_divs(i)
        if len(s) > mx:
            mx=len(s)

    for i in range(start,end+1):
        if len(prime_divs(i))==mx:
            print(i, mx)
            break
