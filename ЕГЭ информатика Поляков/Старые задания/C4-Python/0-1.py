﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-0-1. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
В первой строке сообщается количество учащихся N, каждая из следующих 
N строк имеет формат: 
    <Фамилия> <Инициалы> <номер школы>
где <Фамилия> – строка, состоящая не более чем из 20 символов,
<Инициалы> – строка, состоящая из 4-х символов (буква, точка, буква,
точка), <номер школы> – не более чем двузначный номер. <Фамилия> и
<Инициалы>, а также <Инициалы> и <номер школы> разделены одним
пробелом. Пример входной строки: 
    Иванов П.С. 57 
Требуется написать как можно более эффективную программу, которая будет
выводить на экран информацию, из какой школы было
меньше всего участников (таких школ может быть несколько). При этом
необходимо вывести информацию только по школам, пославшим хотя бы
одного участника. Следует учитывать, что N>=1000.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/0-1.in")

N = int(input())
schCount = {}
for i in range(N):
    fam, io, school = input().split()
    schCount[school] = schCount.get(school, 0) + 1
minCount = min(schCount.values())
schMin = [x[0] for x in list(schCount.items()) if x[1] == minCount]
for x in sorted(schMin):
    print(x)

sys.stdin = save_stdin