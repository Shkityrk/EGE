
s = '564' * 121
while '56' in s or '4444' in s:
    if '56' in s:
        s =s.replace('56' , '4', 1)
        s =s.replace('4444', '4', 1)
print(s)