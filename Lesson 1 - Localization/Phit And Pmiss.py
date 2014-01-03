#Write a code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

for each in range(0,5):
    if each == 0 or each == 3 or each == 4:
        p[each] = p[each]*pMiss
    else:
        p[each] = p[each]*pHit
    

print p
