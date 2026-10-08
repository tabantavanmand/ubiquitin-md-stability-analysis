import matplotlib.pyplot as plt

def read_xvg(filename):
    """Read time and values from a GROMACS .xvg file."""
    time, value = [], []
    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith(('@', '#')):
                cols = line.split()
                if len(cols) >= 2:
                    time.append(float(cols[0]))
                    value.append(float(cols[1]))

    # Auto-detect ps vs ns: if max time > 50, data is in ps -> convert to ns
    if len(time) > 0 and max(time) > 50:
        time = [t / 1000.0 for t in time]

    return time, value

# --- RMSD Comparison: WT vs I36A ---
t_wt, rmsd_wt = read_xvg('../ubiquitin_clean/rmsd.xvg')
t_mut, rmsd_mut = read_xvg('rmsd_i36a_backbone.xvg')

plt.figure(figsize=(10, 6))
plt.plot(t_wt, rmsd_wt, label='Wild-Type (WT)', color='#2A9D8F', linewidth=1.5, alpha=0.85)
plt.plot(t_mut, rmsd_mut, label='Mutant (I36A)', color='#E76F51', linewidth=1.5, alpha=0.85)
plt.title('Backbone RMSD Comparison: WT vs I36A', fontsize=14, fontweight='bold')
plt.xlabel('Time (ns)', fontsize=12)
plt.ylabel('RMSD (nm)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('rmsd_comparison.png', dpi=300)
plt.close()

print("Success: rmsd_comparison.png created successfully!")
