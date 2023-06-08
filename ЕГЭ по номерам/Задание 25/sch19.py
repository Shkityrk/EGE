from fnmatch import *

for n in range(0,10**6+1,61):
    if fnmatch(str(n), '31*2?9*'):
        print(n)