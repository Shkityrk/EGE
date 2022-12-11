for x in range(26):
    for y in range(26):
        r=26**4+3*26**3+y*26**2+x*26+5+2*26**4+4*26**3+y*26**2+26+3
        if r%8==0:
            print(x,y,r//8)