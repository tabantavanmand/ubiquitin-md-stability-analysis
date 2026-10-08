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
                try:
                    x.append(float(parts[0]))
                    y.append(float(parts[1]))
                except ValueError:
                    continue
    return x, y

# 1. RMSD Plot
x_rmsd, y_rmsd = read_xvg('rmsd.xvg')
if x_rmsd and max(x_rmsd) > 50:
    x_rmsd = [val / 1000.0 for val in x_rmsd]

plt.figure(figsize=(8, 5))
plt.plot(x_rmsd, y_rmsd, color='blue', linewidth=1.5)
plt.title('WT Ubiquitin - Backbone RMSD', fontsize=14)
plt.xlabel('Time (ns)', fontsize=12)
plt.ylabel('RMSD (nm)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('rmsd.png', dpi=300)
plt.close()
print("Generated: rmsd.png")

# 2. RMSF Plot (Time-based / Sequence Time)
x_rmsf, y_rmsf = read_xvg('rmsf.xvg')
if x_rmsf and max(x_rmsf) > 50:
    x_rmsf = [val / 1000.0 for val in x_rmsf]

plt.figure(figsize=(8, 5))
plt.plot(x_rmsf, y_rmsf, color='red', linewidth=1.5)
plt.title('WT Ubiquitin - RMSF', fontsize=14)
plt.xlabel('Time (ns)', fontsize=12)
plt.ylabel('RMSF (nm)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('rmsf.png', dpi=300)
plt.close()
print("Generated: rmsf.png")

# 3. Radius of Gyration Plot
x_gyr, y_gyr = read_xvg('gyrate.xvg')
if x_gyr and max(x_gyr) > 50:
    x_gyr = [val / 1000.0 for val in x_gyr]

plt.figure(figsize=(8, 5))
plt.plot(x_gyr, y_gyr, color='green', linewidth=1.5)
plt.title('WT Ubiquitin - Radius of Gyration', fontsize=14)
plt.xlabel('Time (ns)', fontsize=12)
plt.ylabel('Radius of Gyration (nm)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('gyrate.png', dpi=300)
plt.close()
print("Generated: gyrate.png")
