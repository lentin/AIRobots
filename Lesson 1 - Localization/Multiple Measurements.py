
#Mo:dify the code so that it updates the probability twice
#and gives the posterior distribution after both 
#measurements are incorporated. Make sure that your code 
#allows for any sequence of measurement of any length.

"""
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        #This is a bool depending on whether the measured color to the current color in question; if so True, else False
        hit = (Z == world[i])
        
        #append the original value * ((True or False) * .6 + (1-(True or False) * .2))
        #So basically, if the color in question matches the measured color, you get:
        #q.append(p[i] * (True * .6 + (1-True) * .2))
        #Which reduces to:
        #q.append(p[i] * (True * .6 + 0 * .2))
        #q.append(p[i] * .6)
        #If it doesn't match, you get:
        #q.append(p[i] * (False * .6 + (1-False) * .2))
        #q.append(p[i] * .2)
        #As far as I can tell, this is an opaque way to handle a conditional, but it is safer than using an if/else block, so I am not going to rewrite it.
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q
print p
"""

#I have made a few changes to the original code to make it more reusable and encapsulated

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
given_measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, in_measurement, in_world, in_pHit, in_pMiss):
    #Update beliefs, given the input data
    q=[]
    for i in range(len(p)):
        hit = (in_measurement == in_world[i])
        q.append(p[i] * (hit * in_pHit + (1-hit) * in_pMiss))
    
    #Then normalize the values
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def senseMultiple(in_measurements, dataSet, in_world, in_pHit, in_pMiss):
    for eachMeasurement in in_measurements:
        dataSet = sense(dataSet, eachMeasurement, in_world, in_pHit, in_pMiss)
    return dataSet

print(senseMultiple(given_measurements, p, world, pHit, pMiss))

