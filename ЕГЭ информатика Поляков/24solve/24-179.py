# Автор: Л. Шастин

'''
Текстовый файл 24-179.txt содержит строку из заглавных букв A, B, C, D, E, F, всего не более чем из 10^6 символов. Определите, сколько встречается комбинаций вида CB*BC, где на
месте "*" может стоять любая буква, кроме A, B и F. В ответе укажите сначала букву, которая чаще всего встречается на месте "*", затем общее количество подходящих комбинаций.
'''

#Решение:

s = str(open('24-179.txt').readline())
chars = {'C':0, 'D':0, 'E':0}
for char in range(len(s)-4):
	if s[char]+s[char+1] == 'CB' and s[char+3]+s[char+4] == 'BC':
		if s[char+2] not in 'ABF':
			chars[(s[char+2])] += 1
print((list([max(chars.items(), key = lambda char: char[1])]))[0][0], sum(chars.values()), sep = '')

#ИЛИ

s = str(open('24-179.txt').readline())
max_chars, chars = ['D', 'E', 'C'], [0, 0, 0]
for char in range(len(s)-4):
	if s[char]+s[char+1] == 'CB' and s[char+3]+s[char+4] == 'BC':
		if s[char+2] not in 'ABF':
			if s[char+2] == 'D': chars[0] += 1
			elif s[char+2] == 'E': chars[1] += 1
			else: chars[2] += 1
print(max_chars[max(enumerate(chars), key = lambda char: char[1])[0]], sum(chars), sep = '')

#Ответ: C6347

