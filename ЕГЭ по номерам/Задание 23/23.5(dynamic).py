a=[0]*100
a[3]=1
for i in range(3, 10):
    if i + 1 <= 10: a[i + 1] += a[i]
    if i + 3 <= 10: a[i + 3] += a[i]
    if i * 2 <= 10: a[i * 2] += a[i]
for i in range(10, 20):
    if i + 1 <= 20: a[i + 1] += a[i]
    if i + 3 <= 20: a[i + 3] += a[i]
    if i * 2 <= 20: a[i * 2] += a[i]
for i in range(20, 30):
    if i + 1 <= 30: a[i + 1] += a[i]
    if i + 3 <= 30: a[i + 3] += a[i]
    if i * 2 <= 30: a[i * 2] += a[i]
print(a[30])
