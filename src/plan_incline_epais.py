
#!/usr/bin/env python3

from pyDhd import *
from utils import *
from vect3d import Vecteur3D, Vecteur3DS

done = False
dhdOpen()


k = 10000
posx = list()
posy = list()
posz = list()

Force_y = list()
temps = list()

t0 = time()

#definition du plan de la normale etc
normal1 = Vecteur3D(0, 1, 0)
normal1.normalise()

tang1   = Vecteur3D(1, 0, 0)
tang1.normalise()

#point de passage du plan1 
point1 =  Vecteur3D(0.001, 0, 0.02)

#point de passage du plan2
pt2  =  Vecteur3D(0.04, -0.03, -0.01)



def plan3D(n, t, p0, pos_hapt):
    #calcul retour haptique pour un plan incliné avec une épaisseur de 2cm 
    if type(n) is not Vecteur3D:
            print("error")
            return 0
            
    if type(pos_hapt) is not Vecteur3D:
            print("error")
            return 0
            
    OP = pos_hapt - p0
    
    #calcul appartenance au plan
    if abs(OP**n.norm())<=0.01:
        
        #determination du sens de force en fonction du produit scalaire
        if OP**n.norm()>=0:
            return(k*((0.01-OP**n.norm())*n.norm()))
        return(k*((-0.01-OP**n.norm())*n.norm()))
    return Vecteur3d(0,0,0) 
       
    
    

while(not done):
    #mesures vitesses positions
    ret, px,py,pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    print (ret,px,py,pz)
    P = Vecteur3D(px, py, pz)
    
    #calcul force feedback
    Retour = plan3D(normal1, tang1, point1, P)

    dhdSetForce(Retour.x,Retour.y,Retour.z)
    
    #stockage données 
    posx = posx + [px]
    posy = posy + [py]
    posz = posz + [pz]
    ret2, fx, fy, fz = dhdGetForce()
    
    Force_y = Force_y + [fy]
    
    temps = temps + [time()-t0]

    done = dhdGetButton(0)
    
#    print(done)
    

#affichage des forces dans le temps, force-position)
figure('force mur')

plot(temps,Force_y,'blue',label='Position Y')

xlabel('temps (s)')
ylabel('Force (N)')
title('force mur')
legend()

fig2 = figure("Py - Fy")
plot(posy, Force_y,'blue')
xlabel('Y')
ylabel('force')
title('Diagramme Force_Position')


fig = figure("3D")
fig3D = fig.gca(projection='3d')
fig3D.scatter(posx,posy,posz,color='blue',marker="o") 
fig3D.set_xlabel('posx')
fig3D.set_ylabel('posy')
fig3D.set_zlabel('posz')
show()
