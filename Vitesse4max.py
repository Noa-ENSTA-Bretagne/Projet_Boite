import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



# Rajouter la 6ème vitesse !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



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

t0=0
tf=200
k=1000
v0=0
w0=0
def euler(t0,tf,v0,k):
    h = (tf-t0)/k
    y1 = v0
    y2 = v0
    y3 = v0
    y4 = v0
    y5 = v0
    y6 = v0
    w1 = w0
    w2 = w0
    w3 = w0
    w4 = w0
    w5 = w0
    w6 = w0
    t = t0
    Y1 = [v0]
    Y2 = [v0]
    Y3 = [v0]
    Y4 = [v0]
    Y5 = [v0]
    Y6 = [v0]
    W1 = [w0]
    W2 = [w0]
    W3 = [w0]
    W4 = [w0]
    W5 = [w0]
    W6 = [w0]
    T= [t0]
    for i in range(k):
        y1 = y1 + h*((couple(3.6*y1,R1)*n/(Rroue*Rdiff*R1)) - delta*m2 - 0.5*p*SCx*(y1**2))/m1
        y2 = y2 + h*((couple(3.6*y2,R2)*n/(Rroue*Rdiff*R2)) - delta*m2 - 0.5*p*SCx*(y2**2))/m1
        y3 = y3 + h*((couple(3.6*y3,R3)*n/(Rroue*Rdiff*R3)) - delta*m2 - 0.5*p*SCx*(y3**2))/m1
        y4 = y4 + h*((couple(3.6*y4,R4)*n/(Rroue*Rdiff*R4)) - delta*m2 - 0.5*p*SCx*(y4**2))/m1
        y5 = y5 + h*((couple(3.6*y5,R5)*n/(Rroue*Rdiff*R5)) - delta*m2 - 0.5*p*SCx*(y5**2))/m1
        y6= y6 + h * ((couple(3.6 * y6, R6) * n / (Rroue * Rdiff * R6)) - delta * m2 - 0.5 * p * SCx * (y6 ** 2)) / m1
        w1 = y1 / (Rdiff * R1 * Rroue * 3.6) * (60 / (2 * np.pi))
        w2 = y2 / (Rdiff * R2 * Rroue * 3.6) * (60 / (2 * np.pi))
        w3 = y3 / (Rdiff * R3 * Rroue * 3.6) * (60 / (2 * np.pi))
        w4 = y4 / (Rdiff * R4 * Rroue * 3.6) * (60 / (2 * np.pi))
        w5 = y5 / (Rdiff * R5 * Rroue * 3.6) * (60 / (2 * np.pi))
        w6 = y6 / (Rdiff * R6 * Rroue * 3.6) * (60 / (2 * np.pi))
        t = t + h
        Y1.append(3.6*y1)
        Y2.append(3.6*y2)
        Y3.append(3.6*y3)
        Y4.append(3.6*y4)
        Y5.append(3.6*y5)
        Y6.append(3.6 * y6)
        W1.append(3.6*w1)
        W2.append(3.6*w2)
        W3.append(3.6*w3)
        W4.append(3.6*w4)
        W5.append(3.6*w5)
        W6.append(3.6*w6)
        T.append(t)
    return(T,Y1,Y2,Y3,Y4,Y5,Y6,W1,W2,W3,W4,W5,W6)

temps,vit1,vit2,vit3,vit4,vit5,vit6,mot1,mot2,mot3,mot4,mot5,mot6=euler(t0,tf,v0,k)
W1=vit1[-1]/(Rdiff*R1*Rroue*3.6)*(60/(2*np.pi)) #regime du moteur en tr/min
W2=vit2[-1]/(R2*Rdiff*Rroue*3.6)*(60/(2*np.pi))
W3=vit3[-1]/(R3*Rdiff*Rroue*3.6)*(60/(2*np.pi))
W4=vit4[-1]/(R4*Rdiff*Rroue*3.6)*(60/(2*np.pi))
W5=vit5[-1]/(R5*Rdiff*Rroue*3.6)*(60/(2*np.pi))
W6=vit6[-1]/(R6*Rdiff*Rroue*3.6)*(60/(2*np.pi))



vit=[]
mot=[]

vit1max=0
vit2max=0
vit3max=0
vit4max=0
vit5max=0

for j in range(len(vit1)):
    if mot1[j]<3000:
        vit.append(vit1[j])
        mot.append(mot1[j])
        vit1max=vit1[j]
    elif mot2[j]<3000:
        vit2[0]
        vit.append(vit2[j])
        mot.append(mot2[j])
        vit2max = vit2[j]
    elif mot3[j]<3000:
        vit.append(vit3[j])
        mot.append(mot3[j])
        vit3max = vit3[j]
    elif mot4[j]<3000:
        vit.append(vit4[j])
        mot.append(mot4[j])
        vit4max = vit4[j]
    elif mot5[j] < 3000:
        vit.append(vit5[j])
        mot.append(mot5[j])
        vit5max = vit5[j]
    else:
        vit.append(vit6[j])
        mot.append(mot6[j])


#tps1=0
#tps2=0
#tps3=0
#tps4=0
#tps5=0
#for j in range(len(vit1)):
#    while vit2[j]<vit1max:
#        tps1 = j
#    while vit3[j] < vit2max:
#        tps2 = j
#    while vit4[j] < vit3max:
#        tps3 = j
#    while vit5[j] < vit4max:
#        tps4 = j
#    while vit6[j] < vit5max:
#        tps5 = j

plt.figure(1)
plt.plot(temps,vit1,'b',label='Vitesse1')
plt.plot(temps,vit2,'r',label='Vitesse2')
plt.plot(temps,vit3,'g',label='Vitesse3')
plt.plot(temps,vit4,'purple',label='Vitesse4')
plt.plot(temps,vit5,'yellow',label='Vitesse5')
plt.plot(temps,vit6,'orange',label='Vitesse6')
#plt.xlim([0,500])
#plt.ylim([0,500])
plt.xlabel('temps (s)')
plt.ylabel('vitesse (km/h)')
plt.title('Evolution de la vitesse')
plt.legend()
print(W1,W2,W3,W4,W5,W6)


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