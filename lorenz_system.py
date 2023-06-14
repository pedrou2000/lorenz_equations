import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Lorenz system
def lorenz(state, t, sigma, beta, rho):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

# Function to generate and plot Lorenz attractor
def plot_lorenz(init_states, sigma=10.0, beta=8.0/3.0, rho=28.0, t_start=0.0, t_end=50.0, dt=0.01):
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Loop over initial states
    for init_state in init_states:
        # Time array
        t = np.arange(t_start, t_end, dt)  # Modify units of time and time steps as needed

        # Solve for the trajectories
        state = odeint(lorenz, init_state, t, args=(sigma, beta, rho))

        ax.plot(state[:,0], state[:,1], state[:,2])
    
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.show()


# Call the function with the desired parameters
plot_lorenz(
    init_states=[[0.1,0,0],[0.0, -3.0, 1.0], ],#, [1.0, 1.0, 1.0],  [0.0, -5.0, 1.0], [2.0, 1.0, 1.0], [2.0, 2.0, 2.0]],
    sigma=10.0, beta=8.0/3.0, rho=40, 
    t_start=0.0, t_end=30.0, dt=0.01
)
