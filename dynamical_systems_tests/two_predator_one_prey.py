import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Model parameters
r = 1
a = 0.1
e = 0.02
m = 0.1
s = 0.02

# The system of differential equations
def system(y, t):
    P, C1, C2 = y
    dP = r*P - a*P*(C1+C2)
    dC1 = e*a*P*C1 - m*C1 - s*C1*C2
    dC2 = e*a*P*C2 - m*C2 - s*C1*C2
    return [dP, dC1, dC2]

# Initial conditions and time grid
initial_conditions = [[50, 1, 1], [100, 10, 10], [50, 80, 80]]
labels = ['Near Extinction', 'High Prey, Low Predators', 'Predators Dominate']
t = np.linspace(0, 200, 1000)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Solve the system and plot for each initial condition
for y0, label in zip(initial_conditions, labels):
    solution = odeint(system, y0, t)
    ax.plot(solution[:,0], solution[:,1], solution[:,2], label=label)

# Set labels and legend
ax.set_xlabel('P')
ax.set_ylabel('C1')
ax.set_zlabel('C2')
ax.legend()

plt.show()
