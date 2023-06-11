f=open('files_compege/27B_2752.txt')
n=int(f.readline())
q=[int(f.readline()) for i in range(5)]
o1=o3=o7=o9=0
count=0
for i in range(n-5):
    x=int(f.readline())
    if x% 10 == 1: count += o3
    if x% 10 == 3: count += o1
    if x% 10 == 7: count += o9
    if x% 10 == 9: count += o7

    if q[0]% 10 == 1:o1+=1
    if q[0]% 10 == 3:o3+=1
    if q[0]% 10 == 7:o7+=1
    if q[0]% 10 == 9:o9+=1
    q.append(x)
    q.pop(0)
print(count)