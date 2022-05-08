'''Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.

1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (36) ИЛИ нашлось (466) ИЛИ нашлось (5666)
  ЕСЛИ нашлось (36) ТО заменить (36, 5) КОНЕЦ ЕСЛИ
  ЕСЛИ нашлось (466) ТО заменить (466, 3) КОНЕЦ ЕСЛИ
  ЕСЛИ нашлось (5666) ТО заменить (5666, 4) КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой выше программы к строке, в которой первая и последняя цифры – 4, а между ними стоит 100 цифр 6? В ответе запишите полученную строку.'''
s='4'+ '6'*100 + '4'
while '36' in s or '466' in s or '5666' in s:
    if '36' in s:
        s=s.replace ('36', '5', 1)
    if '466' in s:
        s=s.replace ('466', '3', 1)
    if '5666' in s:
        s=s.replace ('5666', '4', 1)
print(s)