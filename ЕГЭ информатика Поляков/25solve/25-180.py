# Автор: Л. Шастин

'''
Среди чисел, больших 520000,  найти числа, сумма всех делителей которых, не считая единицы и самого числа, образует палиндромическое
число. Вывести первые пять чисел, удовлетворяющих вышеописанному условию, справа от каждого числа вывести его максимальный делитель.
'''

#Решение:

def is_palindrom(s):
	res1, res2 = [], []
	while s>0:
		s, el = divmod (s, 10)
		res1 = [el] + res1
		res2 += [el]
	return res1 == res2

k = 0
for x in range (520000, 10**10):
	d, sqrt = set(), int(x**0.5)
	for j in range (2, sqrt+1):
		if x%j == 0:
			d |= {j, x//j}
	if len(d) > 0:
		if is_palindrom (sum(d)):
			k += 1
			print (x, max(d))
			if k == 5:
				break

'''
Ответ:
520211 16781
520993 47363
521653 47423
521947 16837
522077 22699
'''