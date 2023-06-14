import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Model parameters
r = 1
a = 0.1
b = 0.02
c = 0.02
e = 0.02
d = 0.1

# The system of differential equations
def system(y, t):
    P, H, C = y
    dP = r*P - a*P*H
    dH = b*a*P*H - c*H*C
    dC = e*c*H*C - d*C
    return [dP, dH, dC]

# Initial conditions and time grid
y0 = [50, 10, 5]
t = np.linspace(0, 200, 1000)

# Solve the system
solution = odeint(system, y0, t)

# Plot the solution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution[:,0], solution[:,1], solution[:,2])
ax.set_xlabel('P')
ax.set_ylabel('H')
ax.set_zlabel('C')
plt.show()
