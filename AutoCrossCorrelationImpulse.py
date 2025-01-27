import numpy as np
import matplotlib.pyplot as plt

# Create two signals with impulses
n_samples = 100
delay = 20  # Delay for the second signal

# Create first impulse signal
signal1 = np.zeros(n_samples)
signal1[40] = 1  # Impulse at position 40

# Create second impulse signal (delayed version)
signal2 = np.zeros(n_samples)
signal2[40 + delay] = 1  # Delayed impulse

# Calculate auto-correlation of signal1
auto_corr = np.correlate(signal1, signal1, mode='full')

# Calculate cross-correlation between signal1 and signal2
cross_corr = np.correlate(signal1, signal2, mode='full')

# Create time axis for plotting
t = np.arange(-(n_samples-1), n_samples)

# Create subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 12))
fig.suptitle('Impulse Signal Analysis')

# Plot first signal
axs[0].stem(range(n_samples), signal1)
axs[0].set_title('Signal 1 (Impulse)')
axs[0].set_xlabel('Sample')
axs[0].set_ylabel('Amplitude')

# Plot second signal
axs[1].stem(range(n_samples), signal2)
axs[1].set_title('Signal 2 (Delayed Impulse)')
axs[1].set_xlabel('Sample')
axs[1].set_ylabel('Amplitude')

# Plot auto-correlation
axs[2].stem(t, auto_corr)
axs[2].set_title('Auto-correlation of Signal 1')
axs[2].set_xlabel('Lag')
axs[2].set_ylabel('Correlation')

# Plot cross-correlation
axs[3].stem(t, cross_corr)
axs[3].set_title('Cross-correlation between Signal 1 and Signal 2')
axs[3].set_xlabel('Lag')
axs[3].set_ylabel('Correlation')

plt.tight_layout()
plt.show()

# Print some key observations
print("\nKey Points:")
print(f"Auto-correlation peak at lag 0: {auto_corr[n_samples-1]}")
print(f"Cross-correlation peak at lag {delay}: {np.max(cross_corr)}")
print(f"Cross-correlation peak location: {np.argmax(cross_corr) - (n_samples-1)}")
