for m in range(1,1000):
    s='1'+'3'*m+'2'*m
    while '12' in s or '13' in s:
        if '12' in s:s=s.replace('12','48',1)
        if '13' in s:s=s.replace('13', '568',1)

    r=int(s)

    if r%23==0:
        print(m)
        break