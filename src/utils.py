#!/usr/bin/env python3
#bibliothèque numeric pour math

from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import axes3d

from time import time, sleep


#bibliothèque vecteur etc.
class Vecteur3d(object):
    """conteneur des donnees d'un vecteur"""
    
    def __init__ (self, x=0, y=0, z=0):
      self.x=x
      self.y=y
      self.z=z
      
    def lst(self):
      return self.x,self.y,self.z
    
    def __add__ (self, other):
        X=self.x+other.x
        Y=self.y+other.y
        Z=self.z+other.z
        return Vecteur3d(X, Y, Z)
        
    def __str__(self):
        st = "Vecteur3d ( %g, %g, %g )" % (self.x, self.y, self.z)
        return st
        
    def __repr__(self):
        st = "Vecteur3d ( %g, %g, %g )" % (self.x, self.y, self.z)
        return st
        
    def __mul__(self, other):
        if type(other)==Vecteur3d:
          return Vecteur3d(self.y*other.z-self.z*other.y, self.z*other.x- self.x*other.z, self.x*other.y- self.y*other.x)
        elif  (type(other)==float) or (type(other)==int):
          return Vecteur3d(other*self.x, other*self.y, other*self.z)
        else:
          raise ("Undefined operands for *")



    def __rmul__(self, other):
        return self*other
     
    def __truediv__(self, other):
        return self * (1/other)
        
    def __floordiv__(self, other):
        return self * (1//other)
    
    def __neg__(self):
        return Vecteur3d(-self.x, -self.y, -self.z)
        
    def __sub__(self, other):
        return self+(-other)
        
    
            
    
    def __pow__(self, other):
        """
        V1**V1 -> scalaire
        V1**n  -> vecteur
        """
        if type(other) == Vecteur3d:
          return (self.x*other.x + self.y*other.y+ self.z*other.z)
            
        elif ( (type(other)==int)  or (type(other)==float)  ):
          return Vecteur3d(self.x**other, self.y**other, self.z**other)  
        else:
          raise ("Undefined operands for **")

    
    def mod(self):
        return (self**self)**(.5)
   
    def norm(self):
        return self / self.mod()
 
    def normed(self):
        mod = self.mod()
        self.x =  (self.x / mod)
        self.y =  (self.y / mod)
        self.z =  (self.z / mod)
 
    def __eq__(self, other):
        if (self.x==other.x) & (self.y==other.y) & (self.z==other.z) :
            return True
        else:
            return False
        

def save(ifile,*args):
  F= open(ifile, "wt")
  nbr = len(args)
  long = len(args[0])
  
  for i in range (0,long):
    for j in range(0,nbr):
      F.write("%s\t" % args[j][i])
    F.write("\n")
    
  F.close()
  
  
  
