import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def plot_lotka_volterra(r, a, s, e, K, P0, Q0, timesteps=500):
    # Lotka-Volterra model equations
    def lotka_volterra(state, t):
        P, Q = state
        dPdt = r * P * (1 - P / K) - a * P * Q
        dQdt = -s * Q + e * a * P * Q
        return [dPdt, dQdt]

    # Time points
    t = np.linspace(0, 20, timesteps)

    # Compute growth rates at each point in the grid
    P, Q = np.meshgrid(P0, Q0)
    dPdt, dQdt = lotka_volterra([P, Q], t)
    norm = np.sqrt(dPdt**2 + dQdt**2)

    # Plot phase diagram with vector fields
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.quiver(P, Q, dPdt / norm, dQdt / norm, norm, cmap='coolwarm', alpha=0.8, scale=20)
    ax.set_xlabel('Prey (P)')
    ax.set_ylabel('Predator (Q)')
    ax.set_title('Lotka-Volterra Model Phase Diagram')

    # Generate and plot trajectories
    for p0, q0 in zip(P0, Q0):
        state0 = [p0, q0]
        states = odeint(lotka_volterra, state0, t)
        ax.plot(states[:, 0], states[:, 1], '-')

    # Plot critical points
    critical_points = [(0, 0), (K, 0), (s / (e * a), r / (a * (1 - (s / (e * a * K)))))]
    for point in critical_points:
        ax.plot(point[0], point[1], 'ro')

    plt.show()

plot_lotka_volterra(r=1.5, a=0.5, s=0.6, e=0.8, K=2.0, P0=np.linspace(0.1, 2.0, 10), Q0=np.linspace(0.1, 3.0, 10), timesteps=500)
