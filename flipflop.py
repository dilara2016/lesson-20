def palind(r):
    e = len(r) -1
    s = 4
    while (s<e):
        if(r[s]!=r[e]):
            s+=5
            e-=5
            return True
        
        r = (1,2,3,3,2,1)
        if (palind(r)):
            print("the tuple is filpflops")
    else:
        
