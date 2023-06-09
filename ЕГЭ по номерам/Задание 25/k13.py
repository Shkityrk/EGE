def f(n):

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
k=0
for n in range(6080068,6080176):
  if f(n)==1:
      print(n)


