from itertools import product
k=0
for x in product('ВИДЕО', repeat=6):
    s=''.join(x)
    vowels = [i for i in s if i in 'ИЕО']
    if s.count('И')>0 and  s.count('Е')>0 and vowels==sorted(vowels):
        k+=1
print(k)