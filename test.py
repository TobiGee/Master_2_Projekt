import urllib
import requests
import numpy as np
import math

f = open("tsp01.data","r")
points = []
#Berechnet die Distanz zwischen zwei Punkten
def distance(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
for el in f.readlines():
    #Einlesen der Punkte
    points.append([float(el.split()[0]),float(el.split()[1]), False]) #False signalisiert, dass Punkt nicht besucht wurde.
#Neigrest Neigbor

#starte beim ersten Element
indexAktiv = 0
nextPoint = 0
reihenfolge = [0]
while True:
    points[indexAktiv][2] = True
    #berechne distanz
    nextDis = 0
    tmpDis = 1000000
    shouldBreak = True
    for el in range(len(points)):
        #print("")
        #print(reihenfolge)
        if(not points[el][2]):
            shouldBreak = False
            nextDis = distance(points[indexAktiv],points[el])
            #print(nextDis)
            if(nextDis<tmpDis):
                tmpDis = nextDis
                nextPoint = el
                print(el)
    if shouldBreak:
        break
    points[nextPoint][2] = True
    reihenfolge.append(nextPoint)
print(reihenfolge)
f.close()
