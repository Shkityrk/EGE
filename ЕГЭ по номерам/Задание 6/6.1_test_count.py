from turtle import *
color('black', 'red')
speed(10000)
begin_fill()
right(45)
for i in range(4):
    forward(30*100)
    right(90)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-100*100,100*100,100):
    for y in range(-100*100,100*100,100):
        item = canvas.find_overlapping(x, y, x ,y)
        if len(item)==1 and item[0] == 5:
            cnt += 1
print(cnt)
done()
exit()