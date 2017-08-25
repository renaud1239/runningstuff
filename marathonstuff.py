
class temps:
    t=0
    def __init__(self,h=0,m=0,s=0):
        self.t=3600*h+60*m+s
    def str(self):
        h=int(self.t/3600)
        m=int(self.t%3600/60)
        s=self.t%60
        st=''
        if h>0:
            st=st+str(h)+' h '
        if m<10:
            st=st+'0'+str(m)+' m '
        else:
            st=st+str(m)+' m '
        if s<10:
            st=st+'0'+str(s)+' s'
        else:
            st=st+str(s)+' s'
        return st

class vitesse:
    v=0
    def __init__(self,d,t):
        self.v=3600*d/t.t
    def str(self):
        st=''
        st=st+str(int(self.v))+'.'
        d=round(self.v*100)%100
        if d<10:
            st=st+'0'+str(d)
        else:
            st=st+str(d)
        st=st+' km/h'
        return st
    
# Vitesses semi :
print('Extrapolation semi vers marathon :')
for h in [1]:
    for m in range(25,35): # CUSTOM : changement de range minute possible.
        t=temps(h,m,0)
        v=vitesse(21,t)
        print(t.str(),'-',v.str(),end=' ')
        t.t=int(1.05*2*t.t)
        v=vitesse(42.195,t)
        print('~>',t.str(),'-',v.str())
    
# Vitesses 10 km :
print('Extrapolation 10 km vers semi vers marathon :')
for h in [0]:
    for m in range(39,45): # CUSTOM : changement de range minute possible.
        for s in [0,30]: # CUSTOM : changement de range seconde possible.
            t=temps(h,m,s)
            v=vitesse(10,t)
            print(t.str(),'-',v.str(),end=' ')
            t.t=int(1.05*21*t.t/10)
            v=vitesse(21,t)
            print('~>',t.str(),'-',v.str(),end=' ')
            t.t=int(1.05*2*t.t)
            v=vitesse(42.195,t)
            print('~>',t.str(),'-',v.str())

# Estimations VMA :
print('Estimations VMA :')        
t=temps(0,19,44) # CUSTOM : meilleur temps sur 5 km.
v=vitesse(5,t)
print(t.str(),'/  5 km (',v.str(),')',end=' => ')
v=vitesse(5,t)
v.v=v.v/0.92
print(v.str(),end=' à ')
v=vitesse(5,t)
v.v=v.v/0.90
print(v.str())

t=temps(0,40,25) # CUSTOM : meilleur temps sur 10 km.
v=vitesse(10,t)
print(t.str(),'/ 10 km (',v.str(),')',end=' => ')
v=vitesse(10,t)
v.v=v.v/0.92
print(v.str(),end=' à ')
v=vitesse(10,t)
v.v=v.v/0.90
print(v.str())

t=temps(1,30,24) # CUSTOM : meilleur temps sur semi.
v=vitesse(21,t)
print(t.str(),'/SM (',v.str(),')',end=' => ')
v=vitesse(21,t)
v.v=v.v/0.90
print(v.str(),end=' à ')
v=vitesse(21,t)
v.v=v.v/0.85
print(v.str())

t=temps(3,18,31) # CUSTOM : temps sur marathon.
v=vitesse(42.195,t)
print(t.str(),'/ M (',v.str(),')',end=' => ')
v=vitesse(42.195,t)
v.v=v.v/0.85
print(v.str(),end=' à ')
v=vitesse(42.195,t)
v.v=v.v/0.80
print(v.str())
        
# VMA vers 10 km :
print('VMA vers 10 km :')
for i in range(13,19): # CUSTOM : changement de range VMA possible.
    for j in [0,0.5]:
        vma=i+j
        v.v=vma
        print(v.str(),end=' - ')
        t=temps()
        t.t=int(3600*10/(0.92*vma))
        v=vitesse(10,t)
        print(t.str(),'(',v.str(),')',end=' à ')
        t.t=int(3600*10/(0.90*vma))
        v=vitesse(10,t)
        print(t.str(),'(',v.str(),')')
        
# VMA vers semi :
print('VMA vers semi :')
for i in range(13,19): # CUSTOM : changement de range VMA possible.
    for j in [0,0.5]:
        vma=i+j
        v.v=vma
        print(v.str(),end=' - ')
        t=temps()
        t.t=int(3600*21/(0.90*vma))
        v=vitesse(21,t)
        print(t.str(),'(',v.str(),')',end=' à ')
        t.t=int(3600*21/(0.85*vma))
        v=vitesse(21,t)
        print(t.str(),'(',v.str(),')')

# VMA vers marathon :
print('VMA vers marathon :')
for i in range(13,19): # CUSTOM : changement de range VMA possible.
    for j in [0,0.5]:
        vma=i+j
        v.v=vma
        print(v.str(),end=' - ')
        t=temps()
        t.t=int(3600*42.195/(0.85*vma))
        v=vitesse(42.195,t)
        print(t.str(),'(',v.str(),')',end=' à ')
        t.t=int(3600*42.195/(0.80*vma))
        v=vitesse(42.195,t)
        print(t.str(),'(',v.str(),')')

print('')
# CUSTOM : changement d'ensemble de valeurs VMA spécifiques possible.        
for vma in [15.62,15.97,16.14,16.49,16.52,16.60,16.80,16.89]:
    v.v=vma
    print(v.str(),end=' - ')
    t=temps()
    t.t=int(3600*42.195/(0.85*vma))
    v=vitesse(42.195,t)
    print(t.str(),'(',v.str(),')',end=' à ')
    t.t=int(3600*42.195/(0.80*vma))
    v=vitesse(42.195,t)
    print(t.str(),'(',v.str(),')')

# Vitesses marathon :
print('Vitesses marathon :')
for h in [3]:
    for m in range(0,20): # CUSTOM : changement de range minute possible.
        t=temps(h,m,0)
        v=vitesse(42.195,t)
        print(t.str(),'-',v.str())
