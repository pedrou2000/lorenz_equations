import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
a = 100 # Productivity growth rate
b = 10  # Bargaining power of workers
n = 2  # Population growth rate

# System of differential equations
def goodwin(Y, t):
    u, w = Y
    du = a - b*w - (a + n)*u
    dw = b*(u - 1)*w
    return [du, dw]

# Time points
t = np.linspace(0, 30, 1000)

# Phase space setup
u_values = np.linspace(-2, 2, 40)
w_values = np.linspace(-2, 2, 40)

# Create a grid
U, W = np.meshgrid(u_values, w_values)

# Compute growth rate at each grid point
dU, dW = np.zeros(U.shape), np.zeros(W.shape)
n, m = U.shape

for i in range(n):
    for j in range(m):
        dY = goodwin([U[i,j], W[i,j]], t)
        dU[i,j] = dY[0]
        dW[i,j] = dY[1]

# Make the direction field plot
plt.figure(figsize=(8, 6))
Q = plt.quiver(U, W, dU, dW, color='r')

# Plot trajectories for different initial conditions
initial_conditions = [[0.1, 0.1], [1, 1], [-0.5, -0.5], [-1, -1], [0.5, -0.5], [-0.5, 0.5], [1.5, 1.5], [-1.5, -1.5]]
for Y0 in initial_conditions:
    Y = odeint(goodwin, Y0, t)
    plt.plot(Y[:,0], Y[:,1])  # plot trajectory

plt.xlabel('Employment Rate (u)')
plt.ylabel('Wage Share (w)')
plt.title('Phase Diagram of Goodwin’s Model')
plt.grid()
plt.show()
