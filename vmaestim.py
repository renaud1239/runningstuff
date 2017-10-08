# -*- coding: utf-8 -*-

import sys
import copy

class temps:
    def __init__(self,h=0,m=0,s=0):
        self.t=3600*h+60*m+s
    def __str__(self):
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
    def __init__(self,d,t):
        self.v=3600*d/t.t
    def __str__(self):
        st=''
        st=st+str(int(self.v))+'.'
        d=round(self.v*100)%100
        if d<10:
            st=st+'0'+str(d)
        else:
            st=st+str(d)
        st=st+' km/h'
        return st

tlst=input('Temps réf. (h/m/s)> ').split('/')
tref=temps(int(tlst[0]),int(tlst[1]),int(tlst[2]))
dref=int(input('Dist. ref.> '))
vref=vitesse(dref,tref)

print('Base :',dref,'@',vref,'(',tref,')')

vmalow=copy.copy(vref)
vmahgh=copy.copy(vref)
if dref==5 :
    vmalow.v=vmalow.v/0.95
    vmahgh.v=vmahgh.v/0.93
elif dref==10:
    vmalow.v=vmalow.v/0.92
    vmahgh.v=vmahgh.v/0.90
elif dref==21:
    vmalow.v=vmalow.v/0.90
    vmahgh.v=vmahgh.v/0.85
else:
    print('Dist. réf. doit être 5, 10 ou 21 km... Sorry :-(')
    sys.exit(0)

print()    
print('VMA entre',vmalow,'et',vmahgh)
print()

print('Intervalle vitesse fractionnés courts(1) (100% VMA) :',vmalow,'à',vmahgh)
vfraclow=copy.copy(vmalow)
vfraclow.v=vfraclow.v*0.95
vfrachgh=copy.copy(vmahgh)
vfrachgh.v=vfrachgh.v*0.95
print('Intervalle vitesse fractionnés semi-longs(2) (95% VMA) :',vfraclow,'à',vfrachgh)
vfraclow=copy.copy(vmalow)
vfraclow.v=vfraclow.v*0.85
vfrachgh=copy.copy(vmahgh)
vfrachgh.v=vfrachgh.v*0.85
print('Intervalle vitesse fractionnés longs(3) (85% VMA) :',vfraclow,'à',vfrachgh)

print()
print('(1) intervalles rapides de 30 s à 1 min.')
print('(2) intervalles rapides de 400 m à 1 km.')
print('(3) intervalles rapides de 6 à 15 min.')
print()

print('Fenêtre marathon : ',end='')
tmarlow=temps()
tmarlow.t=int(3600*42.195/(0.85*vmahgh.v))
vmarhgh=vitesse(42.195,tmarlow)
print(tmarlow,'(',vmarhgh,')',end=' à ')
tmarhgh=temps()
tmarhgh.t=int(3600*42.195/(0.80*vmalow.v))
vmarlow=vitesse(42.195,tmarhgh)
print(tmarhgh,'(',vmarlow,')')
