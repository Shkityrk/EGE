# -*- coding: utf-8 -*-
"""
Модификация всех файлов
"""

import glob
fileList = glob.glob('*.py')

for fileName in fileList:
    fn, ext = fileName.split('.')
    print(fileName)
    f = open(fileName)
    fileStr = f.read().split("\n")
    f.close()
    if fileStr[0] != '"""': continue

    if fileStr[2].startswith('Задача C4'):
        k = 3
        while k < len(fileStr):
            if fileStr[k].rstrip() == '"""': break
            k += 1
        if fileStr[k+1].startswith('import sys'): continue 
        
        fileStr.insert(k+1, 'import sys')
        fileStr.insert(k+2, 'save_stdin = sys.stdin')
        fileStr.insert(k+3, 'sys.stdin = open("in/%s.in")\n' % (fn))
        
        p = len(fileStr)-1
        while len(fileStr[p].strip()) == 0:
            fileStr = fileStr[:p]
            p -= 1

        fileStr.append("\nsys.stdin = save_stdin")
        
        p = len(fileStr)-1
        while p >= 0:
            fileStr[p] = fileStr[p].replace('fin.readline().rstrip()','input()')
            fileStr[p] = fileStr[p].replace('fin.readline()', 'input()')
            if fileStr[p].startswith('fin = open('):
                fileStr = fileStr[:p] + fileStr[p+1:]
            elif fileStr[p].startswith('fin.close()'):
                fileStr = fileStr[:p] + fileStr[p+1:]
            p -= 1
        
        f = open(fileName, "w")
        f.write("\n".join(fileStr))
        f.close()
        #break
  
    
    


