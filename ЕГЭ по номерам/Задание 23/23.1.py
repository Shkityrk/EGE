'''
от числа 2 к 10
'''
def f (curr,end):
    if curr>end: return 0
    if curr==end: return 1
    if curr<end: return f(curr+1,end)+ f(curr*2,end)
print(f(2,10))