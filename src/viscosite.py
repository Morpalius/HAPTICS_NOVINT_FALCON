#!/usr/bin/env python3

from pyDhd import *
from utils import *

done = False
dhdOpen()


#coef de frottement fluide 
c = 0.002

posx = list()
posy = list()
posz = list()

temps = list()

t0 = time()

while(not done):
    #boucle de simulation de frottement visqueux 
    
    #mesure position vitesses
    ret, px,py,pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    print (ret,px,py,pz)
    
    #MAJ 
    posx = posx + [px]
    posy = posy + [py]
    posz = posz + [pz]
    
    temps = temps + [time()-t0]
    
    #calcul frottement visqueux laminaire
    dhdSetForce(-c*vx,-c*vy,-c*vz)
    done=dhdGetButton(0)
    
#    print(done)
    
dhdClose()

#affichage courbe
figure('x y z')
plot(temps,posx,'red',label='Position X')
plot(temps,posy,'blue',label='Position Y')
plot(temps, posz,'green',label='Position Z')

xlabel('temps (s)')
ylabel('Distance (m)')
title('x y z')
legend()
show()
