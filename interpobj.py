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

tlstlow=input('Temps bas (h/m/s)> ').split('/')
treflow=temps(int(tlstlow[0]),int(tlstlow[1]),int(tlstlow[2]))
dreflow=42.195
vreflow=vitesse(dreflow,treflow)

tlsthgh=input('Temps haut (h/m/s)> ').split('/')
trefhgh=temps(int(tlsthgh[0]),int(tlsthgh[1]),int(tlsthgh[2]))
drefhgh=42.195
vrefhgh=vitesse(drefhgh,trefhgh)

print('Base mar. basse :',dreflow,'@',vreflow,'(',treflow,')')
print('Base mar. haute :',drefhgh,'@',vrefhgh,'(',trefhgh,')')

# TM=2*TS*1.05 => TS=TM/(2*1.05).
tsemilow=copy.copy(treflow)
tsemilow.t=round(tsemilow.t/(2*1.05))
vsemilow=vitesse(21,tsemilow)
tsemihgh=copy.copy(trefhgh)
tsemihgh.t=round(tsemihgh.t/(2*1.05))
vsemihgh=vitesse(21,tsemihgh)

print('Base semi basse :',21,'@',vsemilow,'(',tsemilow,')')
print('Base semi haute :',21,'@',vsemihgh,'(',tsemihgh,')')

print()
print('Objectifs temps/vitesse pour distances :')

for d in range(14,40):
    tlow=temps(0,0,round(tsemilow.t+(d-21)*(treflow.t-tsemilow.t)/(42.195-21)))
    vhgh=vitesse(d,tlow)
    thgh=temps(0,0,round(tsemihgh.t+(d-21)*(trefhgh.t-tsemihgh.t)/(42.195-21)))
    vlow=vitesse(d,thgh)
    print(d,'km -',tlow,'(',vhgh,')','à',thgh,'(',vlow,')')
    
def fordist(d):
    s=str(d//100)+'.'
    if d%100<10:
        s=s+'0'+str(d%100)
    else:
        s=s+str(d%100)
    return s

print()    
print('Objectifs distance/vitesse pour temps :')

for m in range(75,160,5):
    t=temps(0,m,0)
    dlow=21+(t.t-tsemihgh.t)*(42.195-21)/(trefhgh.t-tsemihgh.t)
    dhgh=21+(t.t-tsemilow.t)*(42.195-21)/(treflow.t-tsemilow.t)
    print(t,'-',fordist(round(100*dlow)),'km','(',vitesse(dlow,t),')',\
      'à',fordist(round(100*dhgh)),'km','(',vitesse(dhgh,t),')')
    
    
