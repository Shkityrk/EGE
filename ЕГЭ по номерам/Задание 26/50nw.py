'''f=open('data/26-50.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
a.sort()
ans=[]
n_med=a[n//2]
n2_med=a[n//4*3]


for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j])%2==0:
            sr=(a[i]+a[j])//2
            if n_med<sr and n2_med>sr:
                ans.append(sr)
print(len(ans), min(ans))'''
# Открываем файл и считываем данные
with open('data/26-50.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())  # Количество чисел в наборе
numbers = [int(lines[i].strip()) for i in range(1, n+1)]  # Числа из набора

pair_count = 0  # Количество пар
min_average = float('inf')  # Наименьшее среднее арифметическое

# Создаем хэш-таблицу для быстрого доступа к числам из набора
num_hash = {num: True for num in numbers}

# Перебираем все возможные пары чисел
for i in range(n):
    for j in range(i+1, n):
        if (numbers[i] + numbers[j]) % 2 == 0:  # Проверяем, что сумма пары чисел четная
            average = (numbers[i] + numbers[j]) / 2
            lower_half = sum(num < average for num in numbers) >= n // 2  # Проверка половины чисел меньше среднего арифметического
            upper_quarter = sum(num > average for num in numbers) >= n // 4  # Проверка четверти чисел больше среднего арифметического
            if lower_half and upper_quarter:
                pair_count += 1
                min_average = min(min_average, average)

# Выводим результаты
print(pair_count, int(min_average))