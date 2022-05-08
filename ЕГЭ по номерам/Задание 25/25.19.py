start,end=586132, 586430

def allDivs(x):
    divs=[1,x]
    d=2
    while d**2<x:
        if x%d==0:
            divs.append(d)
        d+=1
    return sorted(divs)



minDivs=[]
maxDivs=[]
for n in range(start,end+1):
    divs=allDivs(n)
    if len(divs)>len(maxDivs):
        divs
