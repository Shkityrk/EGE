'''
x+1
x*2
проходит через 8
от2 до 20
'''


def f(curr,end):
    if curr>end: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+f(curr*2,end)

print(f(2,8)*f(8,20))

