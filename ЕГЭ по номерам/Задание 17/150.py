f = open('data/17-1.txt')
mn = 999999
k = 0
ns = []
h = [int(n) for n in f.readlines()]
for i in range(len(h)-2):
    a = h[i]
    b = h[i+1]
    c = h[i+2]
    if a < b > c:
        k += 1
        ns.append(i+1)

for i in range(len(ns)-1):
    mn = min(ns[i+1] - ns[i], mn)

    
print(mn, k)       
        
        

