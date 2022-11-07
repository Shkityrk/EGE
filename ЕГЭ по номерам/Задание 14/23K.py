for x in '0123456789ab':
    a=int(f'3364{x}',11)+int(f'{x}7946',12)
    b=int(f'55{x}87',14)
    if a==b:
        print(b)