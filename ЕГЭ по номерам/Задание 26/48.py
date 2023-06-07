def calculate_k(num1, num2, numbers):
    average = (num1 + num2) / 2  # Среднее арифметическое пары
    k_values = [abs(average - num) for num in numbers]  # Разница между средним арифметическим и числами из набора
    return min(k_values)  # Наименьшая разница

# Открываем файл и считываем данные
with open('data/26-48.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())  # Количество чисел в наборе
numbers = [int(lines[i].strip()) for i in range(1, n+1)]  # Числа из набора

pair_count = 0  # Количество пар с K равным 5
min_average = float('inf')  # Наименьшее среднее арифметическое

# Перебираем все возможные пары чисел
for i in range(n):
    for j in range(i+1, n):
        if (numbers[i] + numbers[j]) % 2 == 0:  # Проверяем, что сумма пары чисел четная
            k = calculate_k(numbers[i], numbers[j], numbers)
            if k == 5:
                pair_count += 1
                average = (numbers[i] + numbers[j]) / 2
                min_average = min(min_average, average)

# Выводим результаты
print(pair_count, int(min_average))


##made in GhatGPT :)))