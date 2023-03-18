
    s='123'*n
    while '21' in s or '31' in s or '32' in s:
        if '21' in s:s=s.replace('21','12',1)
        elif '31' in s: s=s.replace('31','13',1)
        else: s=s.replace('32','23',1)
    if len(s)>51 and  s[51]=='2':
        print(n)
        break