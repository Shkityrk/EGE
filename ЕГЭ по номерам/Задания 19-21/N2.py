def m(h):
    return h+2, h*2

def game(h):
    if h>=25: return 'w'
    if any(game(i) =='w' for i in m(h)): return 'p1'
    if all(game(i)=='p1' for i in m(h)): return 'v1'
    if any(game(i) =='v1' for i in m(h)): return 'p2'
    if all(game(i)=='p1' or game(i)=='p2' for i in m(h)): return 'v2'
for i in range(1,30):
    if game(i)=='v2':
       print(i,game(i))