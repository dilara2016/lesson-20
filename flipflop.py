def palind(r):
    e = len(r) -1
    s = 0
    while (s<e):
        if(r[s]!=r[e]):
            s+=1
            e-=1
            return True
        
        r = (1,2,3,3,2,1)
        if (palind(r)):
            print("the tuple is filpflops")
    else:
        