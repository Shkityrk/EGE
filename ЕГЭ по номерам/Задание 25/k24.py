from fnmatch import *

for n in range(0,10**6,51):
    if fnmatch(str(n),'12*45*'):
        print(n,n//51)