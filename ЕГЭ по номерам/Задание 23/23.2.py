'''
x+1
x*2
от числа 2 к числу 10 но не через 4
'''
def f(curr, end):
    if curr>end or curr==4: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+f(curr*2,end)
print(f(2,16))