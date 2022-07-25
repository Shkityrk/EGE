def f(x,a):
    return ((x%84!=0) or (x%90!=0)) <= (x%a!=0)

for a in range(1,5000):
    if all(f(x,a) for x in range(1,20000)):
        print(a)
        break
# for a in range(1,1000):
#     f=1
#     for x in range(1,10000):
#         f*=((x%84!=0) or (x%90!=0)) <= (x%a!=0)
#     if f==1:
#         print(a)
#         break