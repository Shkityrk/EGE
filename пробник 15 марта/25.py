from fnmatch import *
k=0
for x in range(0,17*10**6+1,161):
    if fnmatch(str(x),'*1?*?68*'):
        k+=1
        if k==502:print(x,x//161)