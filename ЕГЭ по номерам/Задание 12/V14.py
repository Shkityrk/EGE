s='1'+'57'*30
while '157' in s or '1' in s:
    if '157' in s:s=s.replace('157','5757571',1)
    else:s=s.replace('1','57',1)
print(s.count('7'))