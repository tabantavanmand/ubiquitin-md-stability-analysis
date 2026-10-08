import os
import numpy as np
import matplotlib.pyplot as plt

WORKDIR = os.path.expanduser("~/ubiquitin_clean")
INPUT_FILE = os.path.join(WORKDIR, "rmsd.xvg")
OUTPUT_FILE = os.path.join(WORKDIR, "rmsd.png")

def load_xvg(path):
    time_ps = []
    rmsd_nm = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#") or line.startswith("@"):
                continue

            columns = line.split()

            if len(columns) >= 2:
                time_ps.append(float(columns[0]))
                rmsd_nm.append(float(columns[1]))

    return np.array(time_ps), np.array(rmsd_nm)

time_ps, rmsd_nm = load_xvg(INPUT_FILE)
time_ns = time_ps

plt.figure(figsize=(9, 5), dpi=150)
plt.plot(time_ns, rmsd_nm, color="#1565C0", linewidth=1.2)

plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("RMSD (nm)", fontsize=12)
plt.title("WT Ubiquitin - Backbone RMSD", fontsize=13)

plt.xlim(time_ns.min(), time_ns.max())
plt.grid(True, linestyle="--", alpha=0.35)
plt.tight_layout()

plt.savefig(OUTPUT_FILE, dpi=300)
plt.close()

print("RMSD analysis completed")
print("Input:", INPUT_FILE)
print("Output:", OUTPUT_FILE)
print("Frames:", len(time_ns))
print("Time range (ns):", time_ns.min(), "to", time_ns.max())
print("RMSD range (nm):", rmsd_nm.min(), "to", rmsd_nm.max())
