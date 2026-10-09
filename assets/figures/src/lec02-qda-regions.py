"""Figure code: lec02-qda-regions. Decision regions for the 1-D Gaussian example in Section 5.3.

omega_1 = N(0, 1), omega_2 = N(2, 2^2), equal priors. The two boundaries are where
g1(x) = g2(x); they are located on a fine grid (about 1e-5 resolution) and then plotted.
Between the boundaries the decision is omega_1; outside them the decision is omega_2.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def lpdf(x, m, s):
    return -0.5 * np.log(2 * np.pi * s * s) - (x - m) ** 2 / (2 * s * s)


# boundaries: fine grid, used only to locate the sign changes of g1 - g2
xf = np.linspace(-7, 9, 1_600_001)
diff = lpdf(xf, 0, 1) - lpdf(xf, 2, 2)
idx = np.where(np.diff(np.sign(diff)) != 0)[0]
b_lo, b_hi = float(xf[idx[0]]), float(xf[idx[1]])

# plotting grid (coarse enough for fill_between)
x = np.linspace(-7, 9, 1600)
pdf1 = np.exp(lpdf(x, 0, 1))
pdf2 = np.exp(lpdf(x, 2, 2))
inside = (x >= b_lo) & (x <= b_hi)

fig, ax = plt.subplots(figsize=(8.4, 4.2))
ax.fill_between(x[inside], 0, 0.45, color=c1, alpha=0.18, label=r"decide $\omega_1$ (between boundaries)")
ax.fill_between(x[~inside], 0, 0.45, color=c2, alpha=0.18, label=r"decide $\omega_2$ (outside)")
ax.plot(x, pdf1, color=c1, lw=2.0, label=r"$p(x\mid\omega_1)=\mathcal{N}(0,1)$")
ax.plot(x, pdf2, color=c2, lw=2.0, label=r"$p(x\mid\omega_2)=\mathcal{N}(2,2^2)$")
for b in (b_lo, b_hi):
    ax.axvline(b, color="#333333", ls="--", lw=1.2)
    ax.text(b, 0.44, f" $x={b:.3f}$", fontsize=9, va="top", ha="left")
ax.set_xlim(-7, 9)
ax.set_ylim(0, 0.45)
ax.set_xlabel("feature $x$")
ax.set_ylabel("density")
ax.set_title("Quadratic (QDA) decision regions: two boundaries", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-qda-regions.png", dpi=200)
print("saved assets/figures/lec02-qda-regions.png")
print("boundaries:", round(b_lo, 3), round(b_hi, 3))
