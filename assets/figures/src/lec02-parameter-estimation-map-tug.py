"""Figure code: lec02-parameter-estimation-map-tug.

Tug of war between the prior guess mu0 and the sample evidence xbar.
Settings: mu0 = -2.0, xbar = 2.5, sigma^2 = 1.0, sigma_mu^2 = 1.0.
MAP = (mu0 + (sigma_mu^2/sigma^2) N xbar) / (1 + (sigma_mu^2/sigma^2) N).
N = 1 -> weight 1.0, MAP = 0.25, 50.00% toward xbar.
N = 5 -> weight 5.0, MAP = 1.75, 83.33% toward xbar.
N = 50 -> weight 50.0, MAP = 2.4118, 98.04% toward xbar.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"

mu0, xbar, s2, smu2 = -2.0, 2.5, 1.0, 1.0
cases = [(1, "N = 1 (tiny sample)"), (5, "N = 5 (medium sample)"),
         (50, "N = 50 (large sample)")]

fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.6))

for ax, (n, title) in zip(axes, cases):
    w = smu2 / s2 * n
    mapv = (mu0 + w * xbar) / (1 + w)
    frac = w / (1 + w)
    ax.plot([mu0, xbar], [0.0, 0.0], color="#bbbbbb", lw=6, solid_capstyle="round", zorder=1)
    ax.plot([mu0], [0.0], "o", color=c1, ms=12, zorder=3)
    ax.plot([xbar], [0.0], "o", color=c2, ms=6 + 2.2 * np.log10(n + 1) * 2, zorder=3)
    ax.plot([mapv, mapv], [0.0, 0.28], color="#333333", lw=0.9, zorder=3)
    ax.plot([mapv], [0.32], "v", color="#333333", ms=11, zorder=4)
    ax.annotate(r"$\mu_0=-2.0$" "\n" f"weight 1.0", (mu0, 0.0),
                textcoords="offset points", xytext=(-6, 34), fontsize=8.5,
                color=c1, ha="center")
    ax.annotate(r"$\bar{x}=2.5$" "\n" f"weight {n:.1f}", (xbar, 0.0),
                textcoords="offset points", xytext=(0, -46), fontsize=8.5,
                color=c2, ha="center")
    ax.annotate(r"$\hat{\mu}_{MAP}$" f" $= {mapv:.4f}$", (mapv, 0.32),
                textcoords="offset points", xytext=(0, 14), fontsize=8.5,
                color="#333333", ha="center")
    ax.set_title(f"{title}\n{frac * 100:.2f}% toward the data", fontsize=9.5)
    ax.set_xlim(-3.2, 3.6)
    ax.set_ylim(-1.0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel(r"value of $\mu$")
    ax.grid(axis="x", alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-parameter-estimation-map-tug.png", dpi=200)
print("saved assets/figures/lec02-parameter-estimation-map-tug.png")
for n, _ in cases:
    w = smu2 / s2 * n
    print("N", n, "weight", w, "MAP", round((mu0 + w * xbar) / (1 + w), 4),
          "frac", round(w / (1 + w), 4), "dist-to-mu0 frac", round(1 / (1 + w), 4))
