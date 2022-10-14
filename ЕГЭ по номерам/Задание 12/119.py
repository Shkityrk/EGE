s='5'*93
while '333' in s or '555' in s:
    if '555' in s: s=s.replace('555','3')
    else:s=s.replace('333','5')
print(s)
