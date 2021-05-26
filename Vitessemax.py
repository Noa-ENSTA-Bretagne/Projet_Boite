import numpy as np
import matplotlib.pyplot as plt


m = 987 # Masse du véhicule
Cm= 80 # Couple moteur
n= 0.9 # Rendement  (à confirmer)
Rdiff= 0.25  # Rapport du différentiel     (à confirmer)

Rroue= 0.5*(0.65*2*0.165 + 0.3556) # Rayon de la roue

#Cx=0.3 # Coefficient de la muerte
#S= 1.47 * 1.62 # Surface du véhicule
SCx=0.59

p= 1.292 # Masse volumique de l'air
delta= 0.100 # Résistance au roulement


t0=0
tf=20
n=1000
v0=0
def euler(t0,tf,v0,n):
    h = (tf-t0)/n
    y1 = v0
    y2 = v0
    y3 = v0
    y4 = v0
    y5 = v0
    t = t0
    Y1 = [v0]
    Y2 = [v0]
    Y3 = [v0]
    Y4 = [v0]
    Y5 = [v0]
    T= [t0]
    for k in range(n):
        #if T[-1]<2:
        y1 = y1 + h*((Cm*n/Rroue*Rdiff*1) - delta*m - 0.5*p*SCx*(y1**2))/m
        #elif T[-1]<4:
        y2 = y2 + h*((Cm*n/Rroue*Rdiff*2) - delta*m - 0.5*p*SCx*(y2**2))/m
        #elif T[-1]<6:
        y3 = y3 + h*((Cm*n/Rroue*Rdiff*3) - delta*m - 0.5*p*SCx*(y3**2))/m
        #elif T[-1]<8:
        y4 = y4 + h*((Cm*n/Rroue*Rdiff*4) - delta*m - 0.5*p*SCx*(y4**2))/m
        #else:
        y5 = y5 + h*((Cm*n/Rroue*Rdiff*5) - delta*m - 0.5*p*SCx*(y5**2))/m
        t = t + h
        Y1.append(y1)
        Y2.append(y2)
        Y3.append(y3)
        Y4.append(y4)
        Y5.append(y5)
        T.append(t)
    return(T,Y1,Y2,Y3,Y4,Y5)

temps,vit1,vit2,vit3,vit4,vit5=euler(t0,tf,v0,n)

plt.figure(1)
plt.plot(temps,vit1)
plt.plot(temps,vit2)
plt.plot(temps,vit3)
plt.plot(temps,vit4)
plt.plot(temps,vit5)
#plt.xlim([0,500])
#plt.ylim([0,500])
plt.xlabel('temps')
plt.ylabel('vitesse')
plt.title('hum')

plt.show()



