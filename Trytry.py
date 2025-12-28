import matplotlib.pyplot as plt
import numpy as np

# Time from 0 to 20 years
t = np.linspace(0, 20, 100)

# Model: Exponential decay with a residual value
# V(t) = (Initial_Value - Residual) * e^(-k*t) + Residual
# Let's assume Initial = $30,000, Residual = $2,000, decay rate k = 0.2
V = (30000 - 2000) * np.exp(-0.25 * t) + 2000

plt.figure(figsize=(8, 5))
plt.plot(t, V, color='blue', linewidth=2)
plt.title('Market Value of a Car over 20 Years')
plt.xlabel('Time (Years)')
plt.ylabel('Value ($)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.ylim(0, 31000)
plt.xlim(0, 20)
plt.annotate('Initial Value', xy=(0, 30000), xytext=(2, 25000),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Rapid Depreciation', xy=(2, 18000), xytext=(5, 20000),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('Residual/Scrap Value', xy=(18, 2500), xytext=(12, 8000),
             arrowprops=dict(facecolor='black', shrink=0.05))

print("Displaying graph...")
plt.show()