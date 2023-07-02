for x in '0123456789abcdefghijklm':
    s=int(f'98{x}79641',22)+int(f'25{x}49',22)+int(f'63{x}5',22)
    if s%21==0:
        print(s,s//21)