import numpy as np
import matplotlib.pyplot as plt

#Sample Data

tt= np.linspace(0, 10, 100)

#Sample time points

y0 = 1.0

#Initial value

k = 0.1

#Decay constant

yy = y0*np.exp(-k*tt) #sample solution

#calculation of exact result

tt=np.array(tt)

exact=y0*np.exp(-k*tt)

#plotiing Solution with exact result

plt.subplot(2,1,1)

plt.plot(tt, yy, 'k--', label="exact solution")

plt.xlabel("time")

plt.ylabel("y")

plt.legend(loc='best')

#Plotting Absolute Error

diff=exact - yy

plt.subplot(2,1,2)

plt.plot(tt, diff, 'k', label="Absolute error")

plt.xlabel("time")

plt.ylabel("Error")
plt.legend(loc='best')

plt.title("ODE by Euler method")
plt.savefig("decay-euler.png")
plt.show()