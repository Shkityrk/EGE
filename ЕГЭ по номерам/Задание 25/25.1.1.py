for c1 in '0123456789':
    for c2 in '0123456789':
        a=int(f'23{c1}456{c2}89')
        if a%17==0:
            print(a, a//17)