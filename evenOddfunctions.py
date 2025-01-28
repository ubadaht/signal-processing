import numpy as np
import matplotlib.pyplot as plt

# Create x values from -π to π for better trigonometric visualization
x = np.linspace(-np.pi, np.pi, 400)

# Define the functions and their symmetry properties
functions = [
    (lambda x: x**2, 'y = x²', 'Even'),
    (lambda x: x**3, 'y = x³', 'Odd'),
    (lambda x: np.sin(x), 'y = sin(x)', 'Odd'),
    (lambda x: np.cos(x), 'y = cos(x)', 'Even'),
    (lambda x: np.abs(x), 'y = |x|', 'Even')
]

# Create figure with subplots
plt.figure(figsize=(14, 8))

# Plot each function
for idx, (func, label, symmetry) in enumerate(functions, 1):
    plt.subplot(2, 3, idx)
    
    # Calculate function values
    y = func(x)
    y_flipped = func(-x)
    
    # Plot original and transformed functions
    plt.plot(x, y, 'b-', linewidth=2, label='Original')
    plt.plot(x, y_flipped, 'r--', linewidth=2, label='f(-x)')
    
    # Add symmetry lines
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Formatting
    plt.title(f'{label}\n({symmetry} Function)', fontsize=10)
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y', fontsize=8)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=8)
    plt.axis([-np.pi, np.pi, -3, 3])

plt.tight_layout()
plt.show()
