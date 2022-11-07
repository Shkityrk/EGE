for x in '0123456789abcde':
    for y in '0123456789abcde':
        a=int(f'123{x}5',15)+int(f'67{y}9',17)
        if a%131==0: print(x,y,a//131)