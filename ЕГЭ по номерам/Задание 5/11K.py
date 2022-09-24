for n in range(1,10000):
    b=bin(n)[2:]
    k_ch=0
    k_nch=0
    for i in range(len(b)):
        if (i+1)%2==0 and b[i]=='1': k_ch+=1
        if (i+1)%2!=0 and b[i]=='0': k_nch+=1
    r=abs(k_ch-k_nch)
    if r==5:
        print(n)
        break

