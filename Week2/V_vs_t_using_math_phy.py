import matplotlib.pyplot as plt
import numpy as np

m1=float(input("1st mass: ")) #in solar mass units
m2=float(input("2nd mass: ")) #in solar mass units
e=float(input("Eccentricity: "))
a=float(input("Semi major axis: ")) #in AU

#Time Period
T=np.sqrt(a**3/(m1+m2))
t=np.linspace(0,T,1000) #Specific time instants

#Mean Anomaly
M=2*np.pi*t/T

#Newton Raphson for solving Kepler's equation M=E-esinE
E=np.pi #Initial guess
for i in range(0,5):
    E=(M-e*(E*np.cos(E)-np.sin(E)))/(1-e*np.cos(E))

#Calculating orbital velocities(in Km/s) at those instants
fact=(2/(1-e*np.cos(E)))-1
v1=np.sqrt((8.8681e8*m2*m2*fact)/(a*(m1+m2)))/1000
v2=np.sqrt((8.8681e8*m1*m1*fact)/(a*(m1+m2)))/1000

#Plotting
plt.figure(figsize=(16,8))
plt.plot(t,v1,label='Star 1')
plt.plot(t,v2,label='Star 2')
plt.xlabel('Time(years)')
plt.ylabel('Orbital Velocity(km/s)')
plt.legend(loc='upper center')
plt.show()
