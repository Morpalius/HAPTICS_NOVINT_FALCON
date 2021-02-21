#!/usr/bin/env python3

from pyDhd import *
from utils import *

done = False
dhdOpen()

F = 10000
xr = 0
yr = -0.0193
zr = 0

k = 10000
posx = list()
posy = list()
posz = list()

Force_y = list()
temps = list()

t0 = time()
collide = False

while(not done):
    
    #script simple de retour haptique pour un mur infini en y = 2cm 
    #mesure des positions
    ret, px,py,pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    print (ret,px,py,pz)
    
    
    #calcul de la force
    if(py <= yr ) : 
        dhdSetForce(0,k*(yr-py),0)
        
    else : 
        dhdSetForce(0,0,0)
        
        
    #stockage des positions et des forces
    posx = posx + [px]
    posy = posy + [py]
    posz = posz + [pz]
    ret2, fx, fy, fz = dhdGetForce()
    
    Force_y = Force_y + [fy]
    
    temps = temps + [time()-t0]

    done = dhdGetButton(0)
    
#    print(done)
    

#affichage des résultats, forces
figure('force mur')

plot(temps,Force_y,'blue',label='Position Y')

xlabel('temps (s)')
ylabel('Force (N)')
title('force mur')
legend()

fig2 = figure("Py - Fy")
plot(posy, Force_y,'blue')
xlabel('Y')
ylabel('Force (N)')
title('Diagramme Force_Position')
show()
