"""Figure code: lec02-maxent-bracket. Over the same domain [0, 2], more shape means
less entropy; the uniform density is the maximum-entropy choice.

Each candidate density is normalized numerically on a fine grid; its entropy
H = -int p(x) ln p(x) dx is computed on the same grid, not typed in by hand.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"

x = np.linspace(0.0, 2.0, 20001)
dx = x[1] - x[0]


def entropy(f):
    f = np.clip(f, 0.0, None)
    m = f > 0
    return -np.sum(f[m] * np.log(f[m])) * dx


def normalized(f):
    return f / (np.sum(f) * dx)


def tri(c, w):
    return np.clip(1.0 - np.abs(x - c) / w, 0.0, None)


uniform = normalized(np.ones_like(x))
bell = normalized(np.exp(-(x - 1.0) ** 2 / (2 * 0.35 ** 2)))
triangular = normalized(tri(1.0, 1.0))
bimodal = normalized(tri(0.6, 0.5) + tri(1.4, 0.5))

curves = [
    ("Uniform", uniform, "#d62728", "-", 2.6),
    ("Unimodal bell", bell, "#6a9fd6", "-", 1.8),
    ("Triangular", triangular, "#e0a24d", "-", 1.8),
    ("Bimodal", bimodal, "#6a4c9c", "-", 1.8),
]

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4))

ax = axes[0]
for name, f, color, ls, lw in curves:
    ax.plot(x, f, color=color, ls=ls, lw=lw, label=name)
ax.set_xlim(0, 2)
ax.set_ylim(0, 1.35)
ax.set_xlabel("$x$")
ax.set_ylabel("density $p(x)$")
ax.set_title("(a) four candidate densities on $[0,2]$", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper right")
ax.grid(alpha=0.3)
ax.text(0.04, 1.22, "more structure $\\rightarrow$ more assumptions",
        fontsize=9, color="#333333")

ax = axes[1]
names = [c[0] for c in curves]
vals = [entropy(c[1]) for c in curves]
colors = [c[2] for c in curves]
ypos = np.arange(len(names))[::-1]
bars = ax.barh(ypos, vals, color=colors, alpha=0.9, edgecolor="#333333", linewidth=0.6)
for b, v in zip(bars, vals):
    ax.text(v + 0.012, b.get_y() + b.get_height() / 2, f"{v:.3f}",
            va="center", fontsize=9)
ax.axvline(np.log(2), color="#d62728", ls=":", lw=1.2)
ax.text(np.log(2) + 0.01, -0.62, r"$H_{max}=\ln 2=0.693$", ha="left",
        fontsize=8.5, color="#d62728")
ax.set_yticks(ypos, names, fontsize=9)
ax.set_ylim(-0.95, 3.55)
ax.set_xlim(0, 0.85)
ax.set_xlabel("entropy $H$ (nats)")
ax.set_title("(b) the uniform density has the largest entropy", fontsize=10)
ax.grid(axis="x", alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-maxent-bracket.png", dpi=200)
print("saved assets/figures/lec02-maxent-bracket.png")
for name, f, *_ in curves:
    print(f"{name:14s} area={np.sum(f)*dx:.4f} H={entropy(f):.4f} peak={f.max():.4f}")
print(f"H_max = ln 2 = {np.log(2):.4f}")
