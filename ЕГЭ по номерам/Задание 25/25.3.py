from fnmatch import *
for x in range(0,10**6, 51):
    if fnmatch(str(x), '56*98*'):
        print(x,x//51)