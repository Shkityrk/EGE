"""
Генератор для задачи С4-1
"""
import random
mDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
tAvg =  [-7.8, -7.8, -3.9, 3.1, 9.8, 15.0, 17.8, 16.0, 10.9, 4, 9, -0.3, -5.0, 4.4]
fout = open("1.in", "w")
for m in range(12):
    for d in range(mDays[m]):
        t = random.gauss(tAvg[m], 5)
        print("%02d.%02d %.1f" % (d+1, m+1, t), file = fout)
fout.close()
