import math
        
class Vecteur3D(object):
    def __init__(self, x = 0, y = 0, z = 0):
        """Constructeur avec des valeur par défaut nulles"""
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "Vecteur3D(%g , %g, %g)" % (self.x, self.y, self.z)
        
    def __repr__(self):
        return "Vecteur3D(%g , %g, %g)" % (self.x, self.y, self.z)
        
    def __add__(self, autre): # addition vectorielle
        if type(autre) is Vecteur3D:
            return Vecteur3D(self.x + autre.x, self.y + autre.y, self.z + autre.z)
        if type(autre) is Vecteur3DS:
            tmp = autre.carthesien()
            return Vecteur3D(self.x + tmp.x, self.y + tmp.y, self.z + tmp.z)
    
    def __neg__(self):
        return Vecteur3D(-self.x,-self.y, -self.z)
        
    def __sub__(self,autre):
        return self + (-autre)
    
    def __mul__(self,autre):
        """vectoriel entre 2 vecteur3D, sinon scalaire"""
        if type(autre) is Vecteur3D :
            X = self.y*autre.z - self.z*autre.y
            Y = self.z*autre.x - self.x*autre.z
            Z = self.x*autre.y - self.y*autre.x
            
            return Vecteur3D(X,Y,Z)
            
        elif type(autre) is Vecteur3DS :
            tmp = autre.carthesien()
            return self * tmp
        
        else:
            return Vecteur3D(autre*self.x,autre*self.y,autre*self.z)
    
    def __rmul__(self,autre):
        return self * autre
        
    def __pow__(self,autre):
        """scalaire entre deux Vecteurs3D, puissance entre Vecteur3D et scalaire"""
        if type(autre) is Vecteur3D :
            return self.x * autre.x +self.y * autre.y +self.z * autre.z
        
        else :
            v = self
            for i in range(1,int(autre)):
                if type(v) is Vecteur3D:
                    v = self ** v
                else :
                    v = self * v
            return v
      
    def __truediv__(self,autre):
        return 1/autre * self
        
    def mod(self):
        """La norme du Vecteur3D"""
        return (self**self)**.5
        
    def norm(self):
        """Vecteur Normalisé"""
        m = self.mod()
        if m != 0:
            return self/self.mod()
        else: 
            return 0
        
    def normalise(self):
        """normalisé le vecteur"""
        tmp = self/self.mod()
        self.x = tmp.x
        self.y = tmp.y
        self.z = tmp.z
        
    
        
    def polaire(self):
        """Retourne les coordonnées sphériques r, theta, phi"""

        mod = self.mod()
        theta = math.acos(self.z/mod)
        phi =math.atan2(self.y,self.x)
        
        return Vecteur3DS(mod, theta, phi)
    
    
class Vecteur3DS(object):
    "Classe Vecteur 3d en coordonnées sphériques"""
    def __init__(self,r=0, theta=0, phi=0):
        if r < 0:
            r = -r
            theta = theta + math.pi
        
        self.r = r
        self.theta = theta
        self.phi = phi
        
    def __str__(self):
        return "Vecteur3DS(%g , %g, %g)" % (self.r, self.theta, self.phi)
        
    def __repr__(self):
        return "Vecteur3DS(%g , %g, %g)" % (self.r, self.theta, self.phi)
        
    def __add__(self, autre):
        if type(autre) is Vecteur3D:
            tmp = self.carthesien()
            return (tmp + autre).polaire()
            
        if type(autre) is Vecteur3DS:
            tmp = self.carthesien()
            tmp1 = autre.carthesien()
            return (tmp+tmp1).polaire()
        
        
    def __neg__(self):
        return Vecteur3DS(self.r,self.theta+math.pi,self.phi)
        
        
    def __sub__(self, autre):
        return self + (-autre)
        
    def carthesien(self):
        x = self.r * math.sin(self.theta)*math.cos(self.phi)
        y = self.r * math.sin(self.theta)*math.sin(self.phi)
        z = self.r * math.cos(self.theta)
        return Vecteur3D(x,y,z)
    
    def __mul__(self,autre):
        """vectoriel entre 2 vecteur3DS, sinon scalaire"""
        tmp = self.carthesien()
        res = tmp * autre
        return res.polaire()
    
    def __rmul__(self,autre):
        return self * autre
        
    def __pow__(self,autre):
        """scalaire entre deux Vecteurs3DS, puissance entre Vecteur3D et scalaire"""
        if type(autre) is Vecteur3DS :
            tmp = self.carthesien()
            tmp1 = Vecteur3DS.carthesien()
            return (tmp**tmp1)

        else:
            tmp = self.carthesien()
            tmp1 = tmp ** autre
            if type(tmp1) is Vecteur3D :
                return tmp1.polaire()
            
            else:
                return tmp1
                
    def mod(self):
        return self.r
        
    def norm(self):
        return Vecteur3DS(1,self.theta,self.phi)
        
    def normalise(self):
        self.r = 1
        
        
    
if __name__=="__main__":
    v1 = Vecteur3D(1,1,1)
    v2 = Vecteur3D(1,0,1)        
    vP = Vecteur3DS(1, 1.57,1.57)
    
    print(vP)
    print(vP.carthesien())
      
    #~ print('vectoriel =', v1*v2)
    #~ print('scalaire =', 3 * v1)
    #~ print('scalaire entre v =', v1**v2)
    #~ print('puissance =', v1**3)

    #~ print('la norme = ', v1.mod())
    #~ print('V normalisé =', v1.norm())
    #~ print( 'polaire =',v1.polaire())

    #~ print(v2)
    #~ print(v2.polaire().carthesien())
    #~ print(vP)
    #~ print(vP.carthesien().polaire())
    #~ tmp=v1-vP
    #~ tmp2 = vP - v1
    #~ print(tmp)
    #~ print(tmp2.carthesien())
    
    #~ print(v2*vP)
    #~ print(vP**3)
    
    print(v1.normalise())
    print(v1)
    
