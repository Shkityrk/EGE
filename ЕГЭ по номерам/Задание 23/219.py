a=[0]*10000
a[1]=1
n=0
for i in range(1,9217):
   if 1+i<=9217:
      a[i+1]+=a[i]
      n+=1
      if n==30:
         print(a[9217])
         break
   if i*2<=9217:a[i*2]+=a[i]
   if i*3<=9217:a[i*3]+=a[i]
