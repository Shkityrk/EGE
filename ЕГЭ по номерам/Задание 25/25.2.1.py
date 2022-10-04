for c1 in '0123456789':
    a=f'345789{c1}'
    if a%169==0:
        print(a,a//169)
