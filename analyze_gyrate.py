import matplotlib.pyplot as plt

def moving_average(data, window=50):
    """Simple running average (window in frames) as a guide line only."""
    avg = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        avg.append(sum(data[start:end]) / (end - start))
    return avg

time = []
rg = []

with open('gyrate.xvg', 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith(('#', '@')) or not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            time.append(float(parts[0]) / 1000.0)   # ps -> ns
            rg.append(float(parts[1]))

plt.figure(figsize=(10, 5.5))
plt.plot(time, rg, color='#1b7837', linewidth=0.8, alpha=0.6,
         label='Raw data (1 ps intervals)')
plt.plot(time, moving_average(rg, 50), color='#d95f02', linewidth=2.2,
         label='Running average (50 ps)')

mean_rg = sum(rg) / len(rg)
plt.axhline(mean_rg, color='black', linestyle=':', linewidth=1,
            label=f'Mean = {mean_rg:.4f} nm')

plt.title('WT Ubiquitin - Radius of Gyration (Rg)', fontsize=14,
          fontweight='bold', pad=12)
plt.xlabel('Time (ns)', fontsize=12)
plt.ylabel('Radius of Gyration (nm)', fontsize=12)
plt.xlim(0, 1.0)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(frameon=True, facecolor='white', loc='lower right')

plt.tight_layout()
plt.savefig('gyrate.png', dpi=300)
plt.close()

print(f"Saved 'gyrate.png' | Mean Rg = {mean_rg:.4f} nm | "
      f"Min = {min(rg):.4f} nm | Max = {max(rg):.4f} nm")
