s=open('data/k7/k7-m21.txt').readline()
k = 0  # кол-во троек букв
index = -1  # индекс каждой буквы в строке
for i in range(len(s) - 2):
    index += 1
    if s[i] < s[i + 1] < s[i + 2]:  # проверка возрастания
        k += 1
        r = index  # индекс 1й буквы в тройке

print(k, r)