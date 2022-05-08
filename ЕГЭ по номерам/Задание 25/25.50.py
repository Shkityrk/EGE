def prime(n):
    return n>1 and all (n%i!=0 for i in range(2,int(n**0.5)+1))
def div(n):
    d=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0 :
            d.append(i)
            d.append(n//i)
    return sorted(d)

for i in range(650001, 800000):
    d=div(i)
    prime_divs= [l for l in d if prime(l)]
    if sum(prime_divs)%100==25:
        print(i,sum(prime_divs) )