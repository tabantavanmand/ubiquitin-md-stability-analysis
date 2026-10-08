import numpy as np
import matplotlib.pyplot as plt

def read_xvg(filename):
    x, y = [], []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(('@', '#')):
                continue
            parts = line.split()
            if len(parts) >= 2:
                x.append(float(parts[0]))
                y.append(float(parts[1]))
    return np.array(x), np.array(y)

time_ps, rg_nm = read_xvg('rg_i36a.xvg')

# Convert time from ps to ns
time_ns = time_ps / 1000.0

plt.figure(figsize=(8, 5), dpi=300)
plt.plot(time_ns, rg_nm, color='purple', linewidth=1.5, label='I36A Mutant')
plt.title('I36A Ubiquitin Mutant - Radius of Gyration', fontsize=12)
plt.xlabel('Time (ns)', fontsize=10)
plt.ylabel('Rg (nm)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('rg_i36a.png', dpi=300)
print("Plot saved as rg_i36a.png")
print(f"Time Range: {time_ns[0]:.2f} to {time_ns[-1]:.2f} ns")
print(f"Average Rg: {np.mean(rg_nm):.3f} nm | Min: {np.min(rg_nm):.3f} | Max: {np.max(rg_nm):.3f}")
