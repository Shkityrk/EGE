s=set()
for x in '0123456789abcdefghijk':
    for y in '0123456789abcdefghijk':
        a=int(f'12{y}{x}9',21)
        b=int(f'36{y}99',21)
        if (a+b)%18==0:
            s.add(x)
for x in s:
    a = int(f'125{x}9', 21)
    b = int(f'36599', 21)
    print((a+b)//18)