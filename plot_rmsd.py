import numpy as np
import matplotlib.pyplot as plt

def read_xvg(filename):
    time_data = []
    rmsd_data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(('@', '#')):
                continue
            parts = line.split()
            if len(parts) >= 2:
                time_data.append(float(parts[0]))
                rmsd_data.append(float(parts[1]))
    return np.array(time_data), np.array(rmsd_data)

# Read the data
time_ps, rmsd_nm = read_xvg('rmsd_i36a_backbone.xvg')

# Convert time from ps to ns
time_ns = time_ps / 1000.0

# Plotting
plt.figure(figsize=(8, 5), dpi=300)
plt.plot(time_ns, rmsd_nm, color='blue', linewidth=1.5, label='I36A Backbone')
plt.title('Backbone RMSD - I36A Mutant', fontsize=12)
plt.xlabel('Time (ns)', fontsize=10)
plt.ylabel('RMSD (nm)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Save plot
plt.savefig('rmsd_i36a.png', dpi=300)
print("Plot saved as rmsd_i36a.png")
