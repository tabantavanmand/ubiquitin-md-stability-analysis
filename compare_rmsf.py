# Comparison of RMSF between Wild-Type and I36A Mutant
import numpy as np
import matplotlib.pyplot as plt

def load_xvg(filepath):
    residues, rmsf = [], []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(('@', '#')):
                continue
            parts = line.split()
            if len(parts) >= 2:
                residues.append(float(parts[0]))
                rmsf.append(float(parts[1]))
    return np.array(residues), np.array(rmsf)

# Load RMSF data
wt_res, wt_rmsf = load_xvg('../ubiquitin_clean/rmsf.xvg')
mut_res, mut_rmsf = load_xvg('rmsf.xvg')

# Plot comparison
plt.figure(figsize=(10, 5), dpi=300)
plt.plot(wt_res, wt_rmsf, label='Wild-Type (WT)', color='#008080', linewidth=1.8)
plt.plot(mut_res, mut_rmsf, label='I36A Mutant', color='#FF6F00', linewidth=1.8, linestyle='--')

# Highlight mutation site
plt.axvline(x=36, color='red', linestyle=':', alpha=0.7, label='Mutation Site (Residue 36)')

plt.title('Ubiquitin RMSF per Residue: WT vs I36A', fontsize=14, fontweight='bold')
plt.xlabel('Residue Number', fontsize=12)
plt.ylabel('RMSF (nm)', fontsize=12)
plt.xlim([1, 76])
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(frameon=True, facecolor='white', edgecolor='none')
plt.tight_layout()

# Save plot
plt.savefig('rmsf_comparison.png')
print("RMSF comparison plot generated successfully!")
