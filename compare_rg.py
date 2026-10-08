# Compare Radius of Gyration: WT vs I36A (time converted to ns)
import numpy as np
import matplotlib.pyplot as plt

def load_xvg(path):
    return np.loadtxt(path, comments=('#', '@', '&'))

wt = load_xvg('../ubiquitin_clean/gyrate.xvg')
i36a = load_xvg('gyrate.xvg')

# Convert ps -> ns
wt_t = wt[:, 0] / 1000.0
i36a_t = i36a[:, 0] / 1000.0

print(f"Mean Rg WT   : {wt[:, 1].mean():.4f} nm")
print(f"Mean Rg I36A : {i36a[:, 1].mean():.4f} nm")

plt.figure(figsize=(10, 5))
plt.plot(wt_t, wt[:, 1], label='Wild-Type (WT)', color='#1b9e77', linewidth=1.5)
plt.plot(i36a_t, i36a[:, 1], label='I36A Mutant', color='#d95f02', linestyle='--', linewidth=1.5)

plt.title('Radius of Gyration (Rg) Comparison: WT vs I36A', fontsize=13, fontweight='bold')
plt.xlabel('Time (ns)', fontsize=11)
plt.ylabel('Rg (nm)', fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(frameon=True)
plt.tight_layout()

plt.savefig('rg_comparison.png', dpi=300)
print("Plot successfully saved as rg_comparison.png")
