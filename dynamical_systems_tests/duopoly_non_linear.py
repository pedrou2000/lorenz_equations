import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def phase_plot(a, b, c, d, q0, t_end=20, size=10, grid_points=30):
    # Reaction functions with delay
    def reaction(q, t):
        q1, q2 = q
        dq1dt = (a - b*q2 - c*q2**2)/2 - q1 + d*np.sin(t)
        dq2dt = (a - b*q1 - c*q1**2)/2 - q2 + d*np.sin(t)
        return [dq1dt, dq2dt]

    # Time points
    t = np.linspace(0, t_end, 100)

    # Phase space setup
    q1 = np.linspace(-size, size, grid_points)
    q2 = np.linspace(-size, size, grid_points)

    # Create a grid
    Q1, Q2 = np.meshgrid(q1, q2)

    # Compute growth rate at each grid point
    dQ1, dQ2 = np.zeros(Q1.shape), np.zeros(Q2.shape)
    n, m = Q1.shape

    for i in range(n):
        for j in range(m):
            q0 = [Q1[i,j], Q2[i,j]]
            sol = odeint(reaction, q0, t)
            dQ1[i,j] = sol[-1,0] - Q1[i,j]
            dQ2[i,j] = sol[-1,1] - Q2[i,j]

    # Make the direction field plot
    plt.figure(figsize=(8, 6))
    Q = plt.quiver(Q1, Q2, dQ1, dQ2, color='r')

    plt.xlabel('q1')
    plt.ylabel('q2')
    plt.title(f'Phase Diagram of Cournot Duopoly: a={a}, b={b}, c={c}, d={d}')
    plt.grid()
    plt.show()

# Use the function with various parameters and initial conditions
phase_plot(a=1, b=10, c=0.01, d=0.1, q0=[0.5, 0.5])
phase_plot(a=1, b=-3, c=0.02, d=0.2, q0=[0.5, 0.5])
phase_plot(a=-1, b=0.2, c=1, d=0.2, q0=[0.7, 0.3])
phase_plot(a=1, b=0.1, c=0.01, d=1, q0=[0.2, 0.8])
