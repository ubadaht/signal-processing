import numpy as np
import matplotlib.pyplot as plt

# Create time axis for tau (lag)
tau = np.linspace(-1, 1, 1000)  # Symmetric around zero

# Create triangular autocorrelation function
phi_uu = np.maximum(1 - np.abs(tau), 0)  # Triangular pulse centered at 0

# Plot settings
plt.figure(figsize=(8, 4))
plt.plot(tau, phi_uu, 'b-', linewidth=2)
plt.title('Autocorrelation of Finite Impulse', fontsize=12)
plt.xlabel(r'$\tau$ (arb. units)', fontsize=10)
plt.ylabel(r'$\phi_{uu}(\tau)$', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(-1.2, 1.2)
plt.ylim(-0.1, 1.1)

# Highlight key features
plt.axvline(0, color='k', linestyle='--', linewidth=0.8)
plt.text(0.05, 0.9, 'Maximum at full overlap\n(tau = 0)', ha='left', va='top')

plt.tight_layout()
plt.show()
