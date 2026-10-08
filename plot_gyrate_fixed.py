import numpy as np
import matplotlib.pyplot as plt

def load_xvg(path):
    t, y = [], []
    with open(path) as f:
        for line in f:
            if line.startswith(('#', '@')):
                continue
            parts = line.split()
            t.append(float(parts[0]))
            y.append(float(parts[1]))
    return np.array(t), np.array(y)

def moving_average(x, window=21):
    if window % 2 == 0:
        window += 1
    if window > len(x):
        window = len(x) // 2 * 2 + 1
    pad = window // 2
    padded = np.pad(x, pad, mode='edge')
    kernel = np.ones(window) / window
    return np.convolve(padded, kernel, mode='valid')

time_ps, rg = load_xvg('/home/user/ubiquitin_clean/gyrate.xvg')
time_ns = time_ps / 1000.0

rg_smooth = moving_average(rg, window=21)

fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
ax.plot(time_ns, rg, color='#B0BEC5', alpha=0.45, linewidth=0.8, label='Raw data')
ax.plot(time_ns, rg_smooth, color='#1B5E20', linewidth=2.0, label='Moving average (21 frames)')
ax.set_xlabel('Time (ns)', fontsize=12)
ax.set_ylabel('Radius of Gyration (nm)', fontsize=12)
ax.set_title('WT Ubiquitin - Radius of Gyration', fontsize=13)
ax.set_xlim(time_ns.min(), time_ns.max())
ax.legend(frameon=False)
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('/home/user/ubiquitin_clean/gyrate.png')
print('Saved: ~/ubiquitin_clean/gyrate.png')
