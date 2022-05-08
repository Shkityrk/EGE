start, end= 266868, 336868

def prost(n):
    for d in range(1,round(n**0.5)+1):
        if n%d==0:
            return False

    return True

kol=0
mx=-1
for i in range(start,end+1):
    for del1 in range(1,round(i**0.5)):
        if prost(del1):
            for del2 in range(1, round(i ** 0.5)):
                if prost(del2):
                    if del1*del2==i:
                        if del1!=del2:
                            kol+=1
                            if i>mx:
                                mx=i
print(kol, mx)
