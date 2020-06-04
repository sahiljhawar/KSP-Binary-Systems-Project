# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:14:32 2020

@author: Mohammad Saad
"""
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import astropy.constants as const
import astropy.units as u
import numpy as np

#Taking inputs
m1=float(input("1st mass: "))*u.M_sun
m2=float(input("2nd mass: "))*u.M_sun
x0=float(input("Initial x-coordinate of 1st star: "))*u.AU
y0=float(input("Initial y-coordinate of 1st star: "))*u.AU
u0=float(input("Initial x-velocity of 1st star: "))*u.km/u.s
v0=float(input("Initial y-velocity of 1st star: "))*u.km/u.s
P=float(input("Enter time scale: "))*u.year

#Solving the ODEs, solutions are provvided in SI units
def deri(state,t):
    G=const.G.value
    M1=m1.to('kg').value
    M2=m2.to('kg').value
    x=state[0]
    y=state[1]
    u=state[2]
    v=state[3]
    M=M1+M2
    r=np.sqrt(x*x+y*y)
    k=G*(M2**3)/((M**2)*(r**3))
    return[u,v,-k*x,-k*y]
t = np.linspace(0,P.to('s').value,1000000)
init=[x0.to('m').value,y0.to('m').value,u0.to('m/s').value,v0.to('m/s').value]
sol=odeint(deri,init,t)

#Storing the solutions in respective arrays
x=sol[:,0]*u.m
y=sol[:,1]*u.m
vx=sol[:,2]*u.m/u.s
vy=sol[:,3]*u.m/u.s

#Orbital velocities
v1=np.sqrt(vx**2+vy**2)
v2=m1*v1/m2

#Plotting Orbital Velocity vs Time
plt.figure(figsize=(16,8))
plt.plot(t/31536000,v1.to('km/s').value,label='Star 1')
plt.plot(t/31536000,v2.to('km/s').value,label='Star 2')
plt.ylabel("Orbital Velocity (in km/s)",fontsize=16)
plt.xlabel("Time (in years)",fontsize=16)
plt.legend(loc='upper center')
plt.grid()
plt.show()

#Plotting the orbits
plt.figure(figsize=(16,8))
plt.plot(x.to('AU').value,y.to('AU').value,label='Star 1')
plt.plot(-m1*(x.to('AU').value)/m2,-m1*(y.to('AU').value)/m2,label='Star 2')
plt.plot(0,0,'x',c='black',label='CoM')
plt.title("Orbits of the Two Stars in Cartesian Coordinates",fontsize=20)
plt.ylabel("Y-coordinate (in AU)",fontsize=12)
plt.xlabel("X-coordinate (in AU)",fontsize=12)
plt.legend(loc='upper right')
plt.grid()
plt.show()


