from fnmatch import *
k=0
for i in range(0,17*10**6,161):
    if fnmatch(str(i),'*1?*?68*'):
        k+=1
        if (k-1)%500==0:
            print(i, i//161)