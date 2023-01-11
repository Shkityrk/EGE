with open("D:\Библиотеки\OneDrive\Документы\dataset_3363_3.txt") as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))