k=0
for n in range(1,80):
    b=bin(n)[2:]
    b+='0' if b.count('1')%2==0 else '1'
    b += '0' if b.count('1') % 2 == 0 else '1'
    r=int(b,2)
    if r<80:
        print(r)
        k+=1

print('Total',k)
        