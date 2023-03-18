with open("data/26-j2.txt") as F:
    n = int(F.readline())
    a = []  # массив хранения всех чисел
    for i in range(n):
        monet = F.readline()  # очередное  число
        a.append(int(monet))



    a.sort()
    m=a[n//2]
    sr=sum(a)/len(a)
    print(m,sr)

    k=0
    for i in range(len(a)):
        if sr<=a[i]<=m:k+=1#больше 5003
    print(sr, m,k)
