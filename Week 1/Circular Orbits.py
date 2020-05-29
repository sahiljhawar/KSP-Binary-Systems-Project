import matplotlib.pyplot as plt
import numpy as np

m1=float(input("1st mass: "))
m2=float(input("2nd mass: "))
T=float(input("Time Period: "))
Vcom=float(input("Velocity of COM: "))

Vorb1=np.cbrt(2*np.pi*6.67e-11*m2*m2*m2/(T*365*24*3600*(m1+m2)*(m1+m2)))
Vorb2=np.cbrt(2*np.pi*6.67e-11*m1*m1*m1/(T*365*24*3600*(m1+m2)*(m1+m2)))

rad1=[] #radial velocity of star1 wrt time
rad2=[] #radial velocity of sta2 wrt time
for t in np.linspace(0,T,1000):
    vr1=Vorb1*np.sin(2*np.pi*t/T)+Vcom
    vr2=Vorb2*np.sin((2*np.pi*t/T)-np.pi)+Vcom
    rad1.append(vr1)
    rad2.append(vr2)

plt.figure()
plt.plot(np.linspace(0,T,1000),rad1,'-r',label="Vrad1")
plt.plot(np.linspace(0,T,1000),rad2,'-b',label="Vrad2")
plt.xlabel("Radial Velocity(m/s)")
plt.ylabel("Time(yrs)")
plt.legend()
plt.show()