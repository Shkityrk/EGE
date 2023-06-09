s='7'*209

while '111' in s or '77' in s:
    if '111' in s:s=s.replace('111','7',1)
    if '77' in s:s=s.replace('77', '17',1)
print(s)