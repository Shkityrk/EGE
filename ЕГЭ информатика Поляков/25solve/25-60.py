# А.Н. Носкин

k=0 # порядковый номер

for i in range(3532160, 3532000-1,-1):
    count = 2 # есть уже делители: 1 и само число
    for j in range(2,round(i**0.5)+1): # поиск других делителей
        if i%j == 0:
            count = 0 
            break # число уже не простое
    if count == 2:
        k +=1
        print(k,i)

