d=set()
def f(curr,step):
    if step==8:
        if 1000<=curr<=1024:
            d.add(curr)
    else:
        f(curr+1, step+1)
        f(curr+5, step+1)
        f(curr*3, step+1)
f(1,0)
print(len(d))