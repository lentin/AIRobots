#moddify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

"""
p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        q.append(p[(i-U)%len(p)])
    return q
    


	pprint move(p, 1)
"""

def move(p, U):
        q = [0]*len(p)
        position = U
        for each in p:
                q[position%len(p)] = float(each)
                position+=1
       #This is ugly, but it works for giving inexact moves. It reads through the array of shifted positions, then replaces nonzero entries
       #and their neighbors with the correct inexact movement values, adding if the neighbors are 0 and multiplying if they are not.
        toTranslate = []
        for each in range(len(q)):
            if q[each] > 0:
                toTranslate.append(each)
        for each in toTranslate:
            q[each] = q[each]*pExact
            if q[(each+1)%len(q)] == 0:
                q[(each+1)%len(q)] = q[(each+1)%len(q)] + pOvershoot
            else:
                q[(each+1)%len(q)] = q[(each+1)%len(q)] * pOvershoot
            if q[(each-1)%len(q)] == 0:
                q[(each-1)%len(q)] = q[(each-1)%len(q)] + pUndershoot
            else:
                q[(each-1)%len(q)] = q[(each-1)%len(q)] * pUndershoot
        return q

print move(p, 1)




