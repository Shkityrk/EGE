def f(curr, end):
    if curr>end: return 0
    if curr==end: return 1;
    if curr<end:return f(curr+1,end)+f(curr+3,end)+f(curr*2,end)
print(f(3,10)*f(10,20)*f(20,30))