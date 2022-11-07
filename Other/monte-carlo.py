from random import random
m=0
n=10000000
for i in range(n):
    x=random()
    y=random()
    if x**2+y**2<=1: m+=1
print(4*m/n)