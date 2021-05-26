import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m1 = 987 # Masse du véhicule en kg
m2 = 0.987 #Masse du véhicule en tonne
Cm= 93 # Couple moteur maxi
n= 0.9 # Rendement  (à confirmer)
Rdiff= 0.25  # Rapport du différentiel     (à confirmer)

Rroue= 0.5*(0.6*2*0.165 + 0.3556) # Rayon de la roue en m


#Cx=0.3 # Coefficient de la muerte
#S= 1.47 * 1.62 # Surface du véhicule
SCx=0.59

p= 1.292 # Masse volumique de l'air en unite SI
delta= 100 # Résistance au roulement en N/tonne


t0=0
tf=400
k=1000
v0=0
def euler(t0,tf,v0,k):
    h = (tf-t0)/k
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
    for i in range(k):
        #if T[-1]<2:
        y1 = y1 + h*((Cm*n/(Rroue*Rdiff*1)) - delta*m2 - 0.5*p*SCx*(y1**2))/m1
        #elif T[-1]<4:
        y2 = y2 + h*((Cm*n/(Rroue*Rdiff*2)) - delta*m2 - 0.5*p*SCx*(y2**2))/m1
        #elif T[-1]<6:
        y3 = y3 + h*((Cm*n/(Rroue*Rdiff*3)) - delta*m2 - 0.5*p*SCx*(y3**2))/m1
        #elif T[-1]<8:
        y4 = y4 + h*((Cm*n/(Rroue*Rdiff*4)) - delta*m2 - 0.5*p*SCx*(y4**2))/m1
        #else:
        y5 = y5 + h*((Cm*n/(Rroue*Rdiff*5)) - delta*m2 - 0.5*p*SCx*(y5**2))/m1
        t = t + h
        Y1.append(3.6*y1)
        Y2.append(3.6*y2)
        Y3.append(3.6*y3)
        Y4.append(3.6*y4)
        Y5.append(3.6*y5)
        T.append(t)
    return(T,Y1,Y2,Y3,Y4,Y5)

temps,vit1,vit2,vit3,vit4,vit5=euler(t0,tf,v0,k)

plt.figure(1)
plt.plot(temps,vit1,'b')
plt.plot(temps,vit2,'r')
plt.plot(temps,vit3,'g')
plt.plot(temps,vit4,'purple')
plt.plot(temps,vit5,'y')
#plt.xlim([0,500])
#plt.ylim([0,500])
plt.xlabel('temps (s)')
plt.ylabel('vitesse (km/h)')
plt.title('Evolution de la vitesse')
plt.show()

# a= -0.5*(p*SCx)
# b=Cm*n/(Rroue*Rdiff*5*m1) -delta*(m2/m1)
# def equation(Y,temps):
#     return a*Y**2 + b
#
# temps1=np.linspace(0,50,1001)
# Y=odeint(equation,[0],temps1)
# plt.figure()
# plt.plot(temps,Y)
# plt.show()