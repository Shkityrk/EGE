chet=[int(x) for x in range(2,20,2)]
nech=[int(x) for x in range(1,20,2)]


for i in range(len(chet)):
    for j in range(len(nech)):
        n=3**chet[i]*5**nech[j]
        if 100000000<=n<=300000000:
            print(n)