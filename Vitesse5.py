import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint




m1 = 1245 # Masse du véhicule en kg
m2 = 1.245 #Masse du véhicule en tonne


Cm= 205 # Couple moteur maxi
n= 0.9 # Rendement  (à confirmer)
Rdiff= 0.28 # Rapport du différentiel     (à confirmer)

Rroue= 0.5*(0.65*2*0.175 + 0.381) # Rayon de la roue en m Pneu 175/65/15(pouce)
R1=14/42
R2=22/43
R3=26/36
R4=34/35
R5=32/28
R6=40/28
#Cx=0.3 # Coefficient de la muerte
#S= 1.47 * 1.62 # Surface du véhicule
SCx=0.63

p= 1.292 # Masse volumique de l'air en unite SI
delta= 100 # Résistance au roulement en N/tonne

def couple(vitess,Rapp):
    mot = vitess/(Rdiff*Rapp*Rroue*3.6)*(60/(2*np.pi))
    if mot < 1000:
        return(80)
    elif 1000< mot < 1800:
        C=0.15769 * mot -78.8
        if C<0:
            return(0)
        else:
            return(C)
    elif mot > 2800:
        C= -0.047222222 * mot + 340
        if C<0:
            return(0)
        else:
            return(C)
    else:
        return(205)

def Rapport(k):
    if k==1:
        return(R1)
    if k==2:
        return(R2)
    if k==3:
        return(R3)
    if k==4:
        return(R4)
    if k==5:
        return(R5)
    if k>=6:
        return(R6)

t0=0
tf=100
k=1000
v0=0
w0=0

def euler(t0,tf,v0,k):
    h = (tf-t0)/k
    y = v0
    w = w0
    t = t0
    Y = [v0]
    W = [w]
    T= [t0]
    Rap=1
    for i in range(k):
        y = y + h*((couple(3.6*y,Rapport(Rap))*n/(Rroue*Rdiff*Rapport(Rap))) - delta*m2 - 0.5*p*SCx*(y**2))/m1
        w = y / (Rdiff * Rapport(Rap) * Rroue * 3.6) * (60 / (2 * np.pi))
        t = t + h
        Y.append(3.6*y)
        W.append(3.6*w)
        T.append(t)
        if 3.6*w > 3000:
            Rap+=1
    return(T,Y,W)

temps,vit,mot=euler(t0,tf,v0,k)









plt.figure(2)
plt.plot(temps,mot,'k',label='Vitesse du moteur')
plt.xlabel('temps (s)')
plt.ylabel('vitesse (tour/min)')
plt.title('Evolution de la vitesse du moteur')

plt.figure(3)
plt.plot(temps,vit,'b',label='Vitesse1')
plt.xlabel('temps (s)')
plt.ylabel('vitesse (km/h)')
plt.title('Evolution de la vitesse')
#a= -0.5*(p*SCx)
#b=Cm*n/(Rroue*Rdiff*5*m1) -delta*(m2/m1)
#def equation(Y,temps):
#    return a*Y**2 + b
#temps1=np.linspace(0,50,1001)
#Y=odeint(equation,[0],temps1)
#plt.figure()

plt.show()