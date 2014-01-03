#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.

"""
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    #
    #ADD YOUR CODE HERE
	#
    return q

print sense(p,Z)
"""

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    #initial data
    pHit = 0.6
    pMiss = 0.2
    world=['green', 'red', 'red', 'green', 'green']
    
    #q is the new array
    q = p
   
    #for each item in the input distribution, if the color matches the measured color, augment it accordingly, else lower it
    for i in range(len(q)):
        if world[i] == Z:
            q[i] = q[i]*pHit
        else:
            q[i] = q[i]*pMiss
    return q

print sense(p,Z)
