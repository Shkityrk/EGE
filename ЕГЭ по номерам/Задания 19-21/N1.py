def m(h):
    return h+2, h*2

def game(h):
    if h>=25: return 'w'
    if game(h+2)=='w' or game(h*2)=='w': return "p1"
    if game(h+2)=='p1' and game(h*2)=='p1': return 'v1'
    if game(h+2)=='v1' or game(h*2)=='v1': return "p2"
    if (game(h+2)=='p1' or game(h+2)=='p2') and (game(h*2)=='p1' or game(h*2)=='p2'): return 'v2'
for i in range(1,30):
    print(i,game(i))