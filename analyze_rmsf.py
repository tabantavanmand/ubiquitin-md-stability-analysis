#!/usr/bin/env python3
# RMSF analysis - WT Ubiquitin (1UBQ)
# Raw data plot, no smoothing

import numpy as np
import matplotlib.pyplot as plt

input_file = "/home/taban/ubiquitin_clean/rmsf.xvg"
output_file = "/home/taban/ubiquitin_clean/rmsf.png"

data = []
with open(input_file) as f:
    for line in f:
        if line.startswith(("#", "@")):
            continue
        parts = line.split()
        if len(parts) >= 2:
            data.append([float(parts[0]), float(parts[1])])

data = np.array(data)
residue = data[:, 0]
rmsf = data[:, 1]

plt.figure(figsize=(10, 5))
plt.plot(residue, rmsf, color="#2a9d8f", linewidth=1.0)
plt.xlabel("Residue Number")
plt.ylabel("RMSF (nm)")
plt.title("WT Ubiquitin - RMSF per Residue")
plt.xlim(residue.min(), residue.max())
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_file, dpi=300)

print("RMSF analysis completed")
print(f"Input: {input_file}")
print(f"Output: {output_file}")
print(f"Residues: {len(residue)}")
print(f"RMSF range (nm): {rmsf.min():.6f} to {rmsf.max():.6f}")
print(f"Residue with max flexibility: {residue[rmsf.argmax()]:.0f}")
