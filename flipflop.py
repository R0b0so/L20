def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
     if(r[s]!=r[e]):
        return False
     s+=1
     e-=1
    return True
r = (1,2,3,4,4,3,2,1)
if (palind(r)):
 print("Tuple is flipflop")
else:
 print("Tuple is not flipflop")