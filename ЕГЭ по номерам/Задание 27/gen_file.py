import random
n=12000000

x=[x for x in range(100_000_000) if x%13!=0 or x%18!=0 or x%6!=0 or x%187!=0 or x%53!=0 or x%9!=0]

# Открываем файл в режиме записи
with open("files_compege/test-2.txt", "w") as file:
    file.write(str(n)+' '+'1000000'+"\n")

    # Записываем 5 миллионов случайных чисел в файл
    for i in range(n):
        number1 = random.randint(1, 100_000)
        number2= x[i]
        number3= random.randint(1000_000, 100000000)


        file.write(str(number1) +' '+ str(number2) +' ' +str(number3) +' '+"\n")