for x in range(102,10**6,51):
    s=str(x)
    if s[:2]=='56' and '98' in s:
        print(x,x//51)
        