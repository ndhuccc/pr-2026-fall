"""Figure code: lec02-nonparametric-histogram-bins.

Histogram density estimates of the same sample with too few, a good number,
and too many bins.  The true density is the two-component mixture
0.5*N(-1.5, 0.4^2) + 0.5*N(1.5, 0.5^2), the same one used in the Parzen figure.
The "good" bin count follows the Freedman-Diaconis rule, computed here (not
typed in):  K = ceil((max-min) / (2*IQR*n^(-1/3))).
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
C_TRUE = "#555555"
C_BAR = "#6a9fd6"

N = 200
SEED = 5

rng = np.random.default_rng(SEED)
comp = rng.random(N) < 0.5
samples = np.where(comp, rng.normal(-1.5, 0.4, N), rng.normal(1.5, 0.5, N))


def true_pdf(x):
    g1 = np.exp(-0.5 * ((x + 1.5) / 0.4) ** 2) / (np.sqrt(2 * np.pi) * 0.4)
    g2 = np.exp(-0.5 * ((x - 1.5) / 0.5) ** 2) / (np.sqrt(2 * np.pi) * 0.5)
    return 0.5 * g1 + 0.5 * g2


lo, hi = -3.5, 4.0
q1, q3 = np.percentile(samples, [25, 75])
iqr = q3 - q1
h_fd = 2 * iqr * N ** (-1 / 3)
k_fd = int(np.ceil((hi - lo) / h_fd))

grid = np.linspace(lo, hi, 800)
pdf = true_pdf(grid)

panels = [
    (4, "(a) too few bins: K = 4"),
    (k_fd, f"(b) good bins: K = {k_fd}"),
    (60, "(c) too many bins: K = 60"),
]

fig, axes = plt.subplots(1, 3, figsize=(11.4, 3.7), sharey=True)
for ax, (k, title) in zip(axes, panels):
    ax.hist(samples, bins=k, range=(lo, hi), density=True,
            color=C_BAR, alpha=0.65, edgecolor="#333333", linewidth=0.6)
    ax.plot(grid, pdf, color=C_TRUE, ls="--", lw=2.0, label="true $p(x)$")
    ax.set_title(title, fontsize=10)
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, 0.85)
    ax.set_xlabel("$x$")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("density estimate $\\hat{p}(x)$")
axes[2].legend(frameon=False, fontsize=9, loc="upper right")
fig.suptitle(f"Histogram density estimate, same {N} samples, seed {SEED}", fontsize=11)
fig.tight_layout()
fig.savefig("assets/figures/lec02-nonparametric-histogram-bins.png", dpi=200)
print("saved assets/figures/lec02-nonparametric-histogram-bins.png")
print(f"N={N} seed={SEED} IQR={iqr:.4f} K_FD={k_fd}")
