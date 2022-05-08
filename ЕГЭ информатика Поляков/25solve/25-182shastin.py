# Автор: Л. Шастин

def prime(num):
    return all(num%j != 0 for j in range (2, int(num**0.5)+1))

elems, i = [2, 1],  0
while True:
    elems.append(elems[i]+elems[i+1])
    if (elems[i]+elems[i+1]) > 10**6 and  (elems[i]+elems[i+1]) < 10**9:
        if prime((elems[i]+elems[i+1])):
            print(i+3, (elems[i]+elems[i+1]))
    if (elems[i]+elems[i+1]) > 10**9:
        break
    i += 1