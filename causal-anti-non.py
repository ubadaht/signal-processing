import numpy as np
import matplotlib.pyplot as plt

# Create time axis and input signal (unit impulse)
n = np.arange(-10, 11)
x = (n == 0).astype(int)  # δ[n] at n=0

# Initialize output signals
y_causal = np.zeros_like(x)
y_anticausal = np.zeros_like(x)
y_non = np.zeros_like(x)

# Define systems
for i in range(len(n)):
    # Causal system: y[n] = x[n] + x[n-1]
    y_causal[i] = x[i] + (x[i-1] if n[i] > -10 else 0)
    
    # Anti-causal system: y[n] = x[n] + x[n+1]
    y_anticausal[i] = x[i] + (x[i+1] if n[i] < 10 else 0)
    
    # Noncausal system: y[n] = x[n-1] + x[n+1]
    prev_val = x[i-1] if n[i] > -10 else 0
    next_val = x[i+1] if n[i] < 10 else 0
    y_non[i] = prev_val + next_val

# Plotting
plt.figure(figsize=(12, 8))

# Causal system plot
plt.subplot(3, 1, 1)
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='Input δ[n]')
plt.stem(n, y_causal, linefmt='r--', markerfmt='rx', basefmt=' ', label='Output')
plt.title('Causal System: y[n] = x[n] + x[n-1]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()

# Anti-causal system plot
plt.subplot(3, 1, 2)
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='Input δ[n]')
plt.stem(n, y_anticausal, linefmt='r--', markerfmt='rx', basefmt=' ', label='Output')
plt.title('Anti-Causal System: y[n] = x[n] + x[n+1]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()

# Noncausal system plot
plt.subplot(3, 1, 3)
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt=' ', label='Input δ[n]')
plt.stem(n, y_non, linefmt='r--', markerfmt='rx', basefmt=' ', label='Output')
plt.title('Noncausal System: y[n] = x[n-1] + x[n+1]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
