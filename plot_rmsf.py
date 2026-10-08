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

residue, rmsf = read_xvg('rmsf_i36a.xvg')

plt.figure(figsize=(10, 5), dpi=300)
plt.plot(residue, rmsf, color='teal', linewidth=1.5, label='I36A Mutant')
plt.axvline(x=36, color='red', linestyle='--', linewidth=1.2, label='Mutation Site (I36A)')

plt.title('I36A Ubiquitin Mutant - RMSF per Residue', fontsize=12)
plt.xlabel('Residue Number', fontsize=10)
plt.ylabel('RMSF (nm)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('rmsf_i36a.png', dpi=300)
print("Plot saved as rmsf_i36a.png")
print(f"Residues: {int(residue[0])} to {int(residue[-1])}")
print(f"Average RMSF: {np.mean(rmsf):.3f} nm | Max RMSF: {np.max(rmsf):.3f} nm at residue {int(residue[np.argmax(rmsf)])}")
