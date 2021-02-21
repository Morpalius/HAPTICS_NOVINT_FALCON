#!/usr/bin/env python3

from pyDhd import *
from utils import *

done = False
dhdOpen()

k = 400
xr = 0
yr = 0
zr = 0

 
posx = list()
posy = list()
posz = list()

temps = list()

t0 = time()

while(not done):
    #mesure position et vitesses
    ret, px,py,pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    print (ret,px,py,pz)
    
    #stockage valeurs
    posx = posx + [px]
    posy = posy + [py]
    posz = posz + [pz]
    
    temps = temps + [time()-t0]
    
    #simulation ressort libre
    dhdSetForce(k*(xr-px),k*(yr-py),k*(zr-pz))
    done=dhdGetButton(0)
    
#    print(done)
    
dhdClose()

#affichage deplacements
figure('x y z')
plot(temps,posx,'red',label='Position X')
plot(temps,posy,'blue',label='Position Y')
plot(temps, posz,'green',label='Position Z')

xlabel('temps (s)')
ylabel('Distance (m)')
title('x y z')
legend()
show()
