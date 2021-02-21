
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

#definition de la droite de la glissiere
normal1 = Vecteur3D(-.2, 0.6, 0.2)
normal1.normalise()

#point de passage de la droite de la glissiere
point1 =  Vecteur3D(0, 0, 0)


def prism(n, p0, pos_hapt):
    #fonction de calcul de retour de force pour une glissière 
    if type(n) is not Vecteur3D:
            print("error")
            return 0
            
    if type(pos_hapt) is not Vecteur3D:
            print("error")
            return 0
    
       
    OP = pos_hapt - p0
    
    #calcul du projeté
    proj = (OP**n)*n
    
    #calcul de PP'
    hauteur = OP - proj
    
    #calcul de force
    force = -k * hauteur
    return force
       
    
    

while(not done):
    ret, px,py,pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    print (ret,px,py,pz)
    P = Vecteur3D(px, py, pz)
    
    #calcul de retour de force
    Retour = prism(normal1,  point1, P)
    print(Retour)
    
    #application de la force de retour
    dhdSetForce(Retour.x,Retour.y,Retour.z)
    
    
    #MAJ des enregistrements de position et force
    posx = posx + [px]
    posy = posy + [py]
    posz = posz + [pz]
    ret2, fx, fy, fz = dhdGetForce()
    
    Force_y = Force_y + [fy]
    
    temps = temps + [time()-t0]
    
    #arrêt de la boucle
    done = dhdGetButton(0)
    
#    print(done)
    

#affichage des positions et des diagrames de forces position
figure('force glissière')

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
