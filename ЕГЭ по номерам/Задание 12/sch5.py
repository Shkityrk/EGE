ln=0


for i in range(151,1000):
    s='2'*i

    while '2222' in s:
        s=s.replace('2222','44',1)
        s = s.replace('444', '22', 1)
    if s.count('2')==4:
        print(i)
        break