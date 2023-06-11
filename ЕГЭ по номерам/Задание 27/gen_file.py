import random
n=5000000

# Открываем файл в режиме записи
with open("files_compege/test.txt", "w") as file:
    file.write(str(n)+"\n")
    # Записываем 5 миллионов случайных чисел в файл
    for _ in range(n):
        number = random.randint(1, 1000000)
        file.write(str(number) + "\n")