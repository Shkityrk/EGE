def summ(x):
    s=0
    while x!=0:
        s+=x%10
        x=x//10
    return s
k=0
for i in range(100,1000):
    if i/summ(i)==13:
        print(i)
        k+=i
print('Total',k)