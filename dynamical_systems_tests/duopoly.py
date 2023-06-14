import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
a = 1
c = 0

# Reaction functions
def reaction(q, t):
    q1, q2 = q
    dq1dt = (a - c)/2 - q2/2 - q1
    dq2dt = (a - c)/2 - q1/2 - q2
    return [dq1dt, dq2dt]

# Time points
t = np.linspace(0, 20, 100)

# Initial conditions and solve ODE for these conditions
q0 = [0.5, 0.5]
q = odeint(reaction, q0, t)

size = 100

# Phase space setup
q1 = np.linspace(-size, size, 30)
q2 = np.linspace(-size, size, 30)

# Create a grid
Q1, Q2 = np.meshgrid(q1, q2)

# Compute growth rate at each grid point
dQ1, dQ2 = np.zeros(Q1.shape), np.zeros(Q2.shape)
n, m = Q1.shape

for i in range(n):
    for j in range(m):
        dQ = reaction([Q1[i,j], Q2[i,j]], t)
        dQ1[i,j] = dQ[0]
        dQ2[i,j] = dQ[1]

# Make the direction field plot
plt.figure(figsize=(8, 6))
Q = plt.quiver(Q1, Q2, dQ1, dQ2, color='r')

# plt.plot(q[:,0], q[:,1], 'b-', label='trajectory') # plot trajectory
plt.xlabel('q1')
plt.ylabel('q2')
plt.legend()
plt.title('Phase Diagram of Cournot Duopoly')
plt.grid()
plt.show()
