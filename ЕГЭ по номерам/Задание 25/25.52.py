'''

Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678],
 которые представляют собой произведение трёх различных простых делителей, оканчивающихся
 на одну и ту же цифру. В ответе запишите количество таких чисел и такое из них, для которого
 разность наибольшего и наименьшего простых делителей минимальна.
'''



start, end =485617, 529678

def divs(n):
    s=[]
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            s.append(d)
            s.append(n//d)
    return sorted(s)

def is_prime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))

n=0
index=0
mn=1000000000000000
for i in range(start,end+1):
    d=divs(i)
    pr=sorted(l for l in d if is_prime(l))
    if len(pr)==3 and pr[0]%10==pr[1]%10==pr[2]%10:
        if pr[0]*pr[1]*pr[2]==i:
            n+=1
            if max(pr)- min(pr) < mn:
                mn= max(pr)- min(pr)
                index=i


print(n, index)