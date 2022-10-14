s='321'*50
while '31' in s or '32' in s:
    if '32' in s:
        s=s.replace('32','3',1)
    else:s=s.replace('31','11',1)
print(s.count('1'))