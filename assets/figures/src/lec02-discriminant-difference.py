"""Figure code: lec02-discriminant-difference. Zero crossings of g(x)=g1(x)-g2(x) are the decision boundaries.

omega_1 = N(0, 1), omega_2 = N(2, 2^2), equal priors (the same example as lec02-qda-regions).
g(x) > 0 means decide omega_1; g(x) < 0 means decide omega_2.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def log_gauss(x, m, s):
    return -0.5 * np.log(2 * np.pi * s * s) - (x - m) ** 2 / (2 * s * s)


# boundaries are located on a fine grid (as in lec02-qda-regions), then the plot uses a coarse grid
xf = np.linspace(-7, 9, 1_600_001)
df = log_gauss(xf, 0.0, 1.0) - log_gauss(xf, 2.0, 2.0)   # ln(P) terms cancel for equal priors
crossings = xf[1:][np.sign(df[1:]) != np.sign(df[:-1])]

x = np.linspace(-7, 9, 1600)
d = log_gauss(x, 0.0, 1.0) - log_gauss(x, 2.0, 2.0)

fig, ax = plt.subplots(figsize=(8.4, 5.0))
ax.plot(x, d, color="#5fb8a8", lw=2.2, label=r"$g(x)=g_1(x)-g_2(x)$")
ax.fill_between(x, 0, d, where=d > 0, color=c1, alpha=0.22, label=r"$g>0$: decide $\omega_1$")
ax.fill_between(x, 0, d, where=d < 0, color=c2, alpha=0.22, label=r"$g<0$: decide $\omega_2$")
ax.axhline(0, color="#333333", lw=1.0)
for b in crossings:
    ax.axvline(b, color="#333333", ls="--", lw=1.1)
    ax.text(b, 6.2, f" $x={b:.3f}$", fontsize=9, va="top", ha="left")
ax.set_xlim(-5, 5.5)
ax.set_ylim(-7, 7)   # clipped on purpose: the shape near the two zero crossings is what matters
ax.set_xlabel("feature $x$")
ax.set_ylabel("$g(x)$")
ax.set_title("Two classes, one function: the zero crossings are the boundaries", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-discriminant-difference.png", dpi=200)
print("saved assets/figures/lec02-discriminant-difference.png")
print("boundaries", np.round(crossings, 3))
