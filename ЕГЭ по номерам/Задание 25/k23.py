from fnmatch import *

for n in range(0,10**9+1,169):
    if fnmatch(str(n),'123*567?'):
        print(n,n//169)