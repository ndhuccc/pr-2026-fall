"""Figure code: lec02-gaussian-1d. The mean sets where the curve sits; sigma sets how wide it is.

The two densities are the lecture Section 5.3 example: N(0, 1) and N(2, 2^2).
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def gauss(x, m, s):
    return np.exp(-(x - m) ** 2 / (2 * s * s)) / (np.sqrt(2 * np.pi) * s)


x = np.linspace(-6, 8, 800)
p1 = gauss(x, 0.0, 1.0)
p2 = gauss(x, 2.0, 2.0)

fig, ax = plt.subplots(figsize=(8.4, 5.0))
ax.plot(x, p1, color=c1, lw=2.2, label=r"$\mathcal{N}(\mu=0,\ \sigma=1)$")
ax.plot(x, p2, color=c2, lw=2.2, label=r"$\mathcal{N}(\mu=2,\ \sigma=2)$")
ax.axvline(0, color=c1, ls="--", lw=1.0)
ax.axvline(2, color=c2, ls="--", lw=1.0)
ax.annotate(r"$\mu_1=0$", (0, 0.40), textcoords="offset points", xytext=(-62, 0), fontsize=9, color=c1)
ax.annotate(r"$\mu_2=2$", (2, 0.40), textcoords="offset points", xytext=(6, 0), fontsize=9, color=c2)
ax.text(-5.8, 0.41, r"larger $\sigma$: flatter, wider", fontsize=9, va="center")
ax.set_xlim(-6, 8)
ax.set_ylim(0, 0.45)
ax.set_xlabel("feature $x$")
ax.set_ylabel("density $p(x)$")
ax.set_title("Mean sets the center; sigma sets the width", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-gaussian-1d.png", dpi=200)
print("saved assets/figures/lec02-gaussian-1d.png")
print("peak values", round(float(p1.max()), 4), round(float(p2.max()), 4))