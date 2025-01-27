import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generate more uniform random signal
np.random.seed(42)  # For reproducibility
n_samples = 1000
t = np.linspace(0, 1, n_samples)

# Create a more uniform signal by combining uniform noise with some random variations
uniform_base = np.random.uniform(-1.5, 1.5, n_samples)
noise = np.random.normal(0, 0.3, n_samples)
original_signal = uniform_base + noise

# Design filters
fs = 1000  # Sample frequency
cutoff = 50  # Cutoff frequency
nyquist = fs / 2
order = 4  # Filter order

# Create Butterworth filters
b_low, a_low = signal.butter(order, cutoff/nyquist, btype='low')
b_high, a_high = signal.butter(order, cutoff/nyquist, btype='high')

# Apply filters
low_passed = signal.filtfilt(b_low, a_low, original_signal)
high_passed = signal.filtfilt(b_high, a_high, original_signal)

# Create subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle('Signal Analysis: Original vs Filtered')

# Plot original signal and its histogram
axs[0, 0].plot(t, original_signal, 'b', linewidth=0.5)
axs[0, 0].set_title('Original Signal')
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Amplitude')

axs[0, 1].hist(original_signal, bins=50, color='b', alpha=0.7)
axs[0, 1].set_title('Original Signal Histogram')
axs[0, 1].set_xlabel('Value')
axs[0, 1].set_ylabel('Count')

# Plot low-pass filtered signal and its histogram
axs[1, 0].plot(t, low_passed, 'g', linewidth=0.5)
axs[1, 0].set_title('Low-Pass Filtered Signal')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Amplitude')

axs[1, 1].hist(low_passed, bins=50, color='g', alpha=0.7)
axs[1, 1].set_title('Low-Pass Filtered Histogram')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Count')

# Plot high-pass filtered signal and its histogram
axs[2, 0].plot(t, high_passed, 'r', linewidth=0.5)
axs[2, 0].set_title('High-Pass Filtered Signal')
axs[2, 0].set_xlabel('Time')
axs[2, 0].set_ylabel('Amplitude')

axs[2, 1].hist(high_passed, bins=50, color='r', alpha=0.7)
axs[2, 1].set_title('High-Pass Filtered Histogram')
axs[2, 1].set_xlabel('Value')
axs[2, 1].set_ylabel('Count')

# Adjust layout
plt.tight_layout()
plt.show()

# Print some statistics
print("\nSignal Statistics:")
print(f"Original Signal - Mean: {np.mean(original_signal):.3f}, Std: {np.std(original_signal):.3f}")
print(f"Low-Pass Signal - Mean: {np.mean(low_passed):.3f}, Std: {np.std(low_passed):.3f}")
print(f"High-Pass Signal - Mean: {np.mean(high_passed):.3f}, Std: {np.std(high_passed):.3f}")
