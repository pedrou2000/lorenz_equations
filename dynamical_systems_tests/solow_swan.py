import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
s = 0.4  # Savings rate
n = 0.02  # Population growth rate
g = 0.01  # Technology growth rate
δ = 0.08  # Depreciation rate
α = 0.33  # Output elasticity of capital

# Production function
def f(k):
    return k**α

# Capital accumulation function
def solow(k, t):
    return s*f(k) - (n + g + δ)*k

# Time points
t = np.linspace(0, 100, 1000)

# Initial conditions and solve ODE for these conditions
k0 = 1
k = odeint(solow, k0, t)

# Phase space setup
k_values = np.linspace(0.5, 2, 100)

# Compute growth rate at each grid point
k_dot = solow(k_values, t)

# Make the direction field plot
plt.figure(figsize=(8, 6))
plt.plot(k_values, k_dot, 'b-', label='dk/dt')
plt.plot(k_values, np.zeros(len(k_values)), 'r--')
plt.plot(k, np.zeros(len(k)), 'g:', label='trajectory')
plt.xlabel('k')
plt.ylabel('dk/dt')
plt.title('Phase Diagram of Solow-Swan Model')
plt.legend()
plt.grid()
plt.show()
    