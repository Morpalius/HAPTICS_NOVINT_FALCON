#!/usr/bin/env python3

from pyDhd import *
from utils import *
from vect3d import Vecteur3D, Vecteur3DS
from time import time
done = False
dhdOpen()


radius = 0.015
xr = 0
yr = 0.01
zr = 0

k = 5000
posx = list()
posy = list()
posz = list()

posx1 = list()
posy1 = list()
posz1 = list()

Pos_rho = list()

cx = list()
cy = list()
cz = list()

Fx = list()
Fy = list()
Fz = list()

temps = list()
Force_p = list()
t0 = time()
collide = False


#param sphère
radius = 0.03
xr = 0
yr = 0.02
zr = 0
Centre = Vecteur3D(xr, yr, zr)

#sphere2
rad2 = 0.03
Centre2 = Vecteur3D(0, 0, 0)


def murY(ym, stiff, pos_hapt):
    
    if(pos_hapt.y <= ym ) : 
        return Vecteur3D(0,stiff*(ym-pos_hapt.y),0)
        
    else : 
        return Vecteur3D(0,0,0)
    
    
def sphereF(Center, rayon, stiff, pos_hapt):
    
    if type(Center) is not Vecteur3D:
            print("error")
            return 0
            
    if type(pos_hapt) is not Vecteur3D:
            print("error")
            return 0
            
    Pos_rel= pos_hapt-Center
    Dist_r = Pos_rel.mod()
    
    Pos_rel.normalise()

    Xs = Pos_rel.x
    Ys = Pos_rel.y
    Zs = Pos_rel.z
    
    d_rho = Dist_r - rayon
    
    print(d_rho)
    if(d_rho < 0):
        F = -stiff*d_rho
        
        return Vecteur3D(F*Xs,F*Ys,F*Zs)
       
    else : 
        return Vecteur3D(0,0,0)
       
        

def springForce(position, stiffness):
    return 0
    
"""  
while(not done):
    ret, px,py,pz = dhdGetPosition()
    ret, vx, vy, vz = dhdGetLinearVelocity()
    print (ret,px,py,pz)
    
    P = Vecteur3D(px, py, pz)
    Retour = sphereF(Centre, radius, k, P)
    Retour = Retour + sphereF(Centre2, rad2, k, P)
    dhdSetForce(Retour.x,Retour.y,Retour.z)
    
    posx1 = posx1 + [px]
    posy1 = posy1 + [py]
    posz1 = posz1 + [pz]
    Pos_rho = Pos_rho +  [sqrt((px - xr)**2 + (py - yr)**2 + (pz - zr)**2)]
    
    ret2, fx, fy, fz = dhdGetForce()
    
    Force_p = Force_p + [sqrt(fx**2 +fy**2 + fz**2)]
    
    Fx = Fx + [fx]
    Fy = Fy + [fy]
    Fz = Fz + [fz]
    
    temps = temps + [time()-t0]

    done = dhdGetButton(0)
    
    print(done)
    

fig = figure("3D")
fig3D = fig.gca(projection='3d')
fig3D.scatter(cx,cy,cz,color='blue',marker="o")
#fig3D.quiver(cx,cy,cz, Fx, Fy, Fz, color='blue',normalize="True")

fig3D.scatter(posx1,posy1,posz1,color='red',marker="+")
#fig3D.set_aspect('equal', adjustable= 'box')
fig3D.set_xlabel('posx')
fig3D.set_ylabel('posy')
fig3D.set_zlabel('posz')

fig3D.autoscale_view()

fig2 = figure("P_rho - F_rho")
plot(Pos_rho, Force_p,'blue')
xlabel('Y')
ylabel('force')
title('Diagramme Force_Position')

#print(fig3D.get_xlim())
show()"""
