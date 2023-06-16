n=0
min_len=10**20
for i in range(51,1000):
    s='1'*i
    while '111' in s:
        s=s.replace('111','22',1)
        s=s.replace('222','11',1)
    if len(s)<min_len:
        min_len=len(s)
        n=i
print(n)