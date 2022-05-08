# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-mark_author. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Проставление информации об авторе
из файла preabmle
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/mark_author.in")


fPre = open("preamble")
preAmble =  fPre.read().split("\n")
fPre.close()

import glob
fileList = glob.glob('*.py')
for fileName in fileList:
    fn, ext = fileName.split('.')
    print(fileName)
    f = open(fileName)
    fileStr = f.read().split("\n")
    f.close()
    if fileStr[0] != '"""': continue
    if fileStr[2].startswith('Задача C4'): continue
    fileStr = fileStr[:1] + preAmble + fileStr[1:]
    fileStr[2] = fileStr[2] % (fn)
    f = open(fileName, "w")
    f.write("\n".join(fileStr))
    f.close()

sys.stdin = save_stdin