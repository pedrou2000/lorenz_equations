import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve


# Model parameters
alpha = 0.3
beta = 0.95
delta = 0.1
rho = 0.05

# Steady state
k_ss_func = lambda k: alpha*beta*(k**(alpha-1)) + 1 - delta - rho
k_ss = fsolve(k_ss_func, 0.1)[0]
c_ss = (alpha*beta*(k_ss**alpha)) / (1 - beta*(1-delta))

# Define system of differential equations
def system(k, t):
    y = k**alpha
    c = (alpha*beta*y) / (1 - beta*(1-delta))
    k_dot = y - delta*k - c
    return k_dot

# Simulate the model
t = np.linspace(0, 50, 1000)
k0 = k_ss
k_vals = odeint(system, k0, t)

# Calculate consumption values
c_vals = (alpha*beta*(k_vals**alpha)) / (1 - beta*(1-delta))

# Plot the phase diagram
plt.plot(t, k_vals, label='Capital')
plt.plot(t, c_vals, label='Consumption')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Dynamics of Capital and Consumption')
plt.show()
