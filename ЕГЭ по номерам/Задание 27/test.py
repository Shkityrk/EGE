k_0_13 =[]
k_0 =[]
k_1_13 =[]
k_1 =[]
for i in range(1,1000):
    if i % 2 == 0 and i % 13 == 0: k_0_13.append(i)
    if i % 2 == 0 and i % 13 != 0: k_0.append(i)
    if i % 2 != 0 and i % 13 == 0: k_1_13.append(i)
    if i % 2 != 0 and i % 13 != 0: k_1.append(i)

print('k_0_13',k_0_13)
print('k_0',k_0)
print('k_1_13',k_1_13)
print('k_1',k_1)