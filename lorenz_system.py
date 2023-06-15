import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Define the Lorenz system
def lorenz(state, t, sigma, beta, rho):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

# Function to generate and plot Lorenz attractor
def plot_lorenz(init_states, trajectory_colors, fixed_point_colors, sigma=10.0, beta=8.0/3.0, rho=28.0, t_start=0.0, t_end=50.0, dt=0.01, save_path='./'):
    # Create a directory for the images if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Generate fixed points
    c = np.sqrt(beta * (rho - 1))
    fixed_points = [(c, c, rho-1), (-c, -c, rho-1)]  
    
    # Generate and save XY, XZ, and YZ projections
    for (x_index, y_index, title) in [(0, 1, 'XY'), (0, 2, 'XZ'), (1, 2, 'YZ')]:
        fig, ax = plt.subplots()

        # Loop over initial states and their colors
        for init_state, color in zip(init_states, trajectory_colors):
            # Time array
            t = np.arange(t_start, t_end, dt)  # Modify units of time and time steps as needed

            # Solve for the trajectories
            state = odeint(lorenz, init_state, t, args=(sigma, beta, rho))

            ax.plot(state[:,x_index], state[:,y_index], color=color)  # use specified color
        
        # Plot fixed points with their colors
        for fixed_point, color in zip(fixed_points, fixed_point_colors):
            ax.scatter(fixed_point[x_index], fixed_point[y_index], color=color)  # use specified color

        ax.set_title(f"Lorenz Attractor {title} Projection")
        fig.savefig(os.path.join(save_path, f'lorenz_attractor_{title}_projection.png'))
        plt.close(fig)  # Close the figure to free up memory

# Call the function with the desired parameters
plot_lorenz(
    init_states=[[0.1,0,0], [-0.1, 0.0, 0.0]],
    trajectory_colors=[(135/255, 206/255, 235/255), (147/255, 112/255, 219/255)],  # Forest Green and Medium Purple
    fixed_point_colors=['black', 'black'],
    sigma=10.0, beta=8.0/3.0, rho=28, 
    t_start=0.0, t_end=30.0, dt=0.01,
    save_path='./lorenz_images'
)


