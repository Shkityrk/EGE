from fnmatch import *

for n in range(0,10**7+1,387):
    if fnmatch(str(n), '*16*9?0?'):
        print(n)