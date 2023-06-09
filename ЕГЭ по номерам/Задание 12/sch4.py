s='6'*149+'1'

while '14' in s or '661' in s:
    if '14' in s:s=s.replace('14','61',1)
    if '661' in s:s=s.replace('661', '14',1)
print(s)