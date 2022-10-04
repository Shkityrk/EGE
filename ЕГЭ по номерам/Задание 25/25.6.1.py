from fnmatch import *
for x in range(0,10**10,121):
    if fnmatch(hex(x)[2:], '1?ded?ced'):
        print(x,x//121)