"""Figure code: lec02-mixture-1d-components.

A mixture density is a weighted sum of component densities. Two 1-D Gaussians,
P1*N(0, 1) + P2*N(3, 0.6^2), give a two-peaked density that one Gaussian cannot match.
The single Gaussian is the maximum-likelihood fit to 600 samples of the mixture
(fixed seed 7). All curves are computed from the analytic formulas, not hand-drawn.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def gauss(x, m, s):
    return np.exp(-(x - m) ** 2 / (2 * s * s)) / (np.sqrt(2 * np.pi) * s)


P1, P2 = 0.6, 0.4
m1, s1 = 0.0, 1.0
m2, s2 = 3.0, 0.6

rng = np.random.default_rng(seed=7)
n = 600
which = rng.random(n) < P1
samp = np.where(which, rng.normal(m1, s1, n), rng.normal(m2, s2, n))
mu_hat = samp.mean()
var_hat = samp.var()

x = np.linspace(-4.5, 5.5, 800)
g1 = gauss(x, m1, s1)
g2 = gauss(x, m2, s2)
mix = P1 * g1 + P2 * g2
fit = gauss(x, mu_hat, np.sqrt(var_hat))

fig, ax = plt.subplots(figsize=(8.6, 5.0))
ax.plot(x, P1 * g1, color=c1, lw=1.6, ls="--", label=r"$P_1\,\mathcal{N}(0,1)$")
ax.plot(x, P2 * g2, color=c2, lw=1.6, ls="--", label=r"$P_2\,\mathcal{N}(3,0.6^2)$")
ax.plot(x, mix, color="#222222", lw=2.6, label=r"mixture $P_1 p_1+P_2 p_2$")
ax.plot(x, fit, color="#8a8a8a", lw=2.2, ls=":", label="one Gaussian (ML fit)")
ax.axhline(0, color="#cccccc", lw=0.8)

ax.text(0.0, 0.250, "peak 1", ha="center", fontsize=9, color="#222222")
ax.text(2.98, 0.288, "peak 2", ha="center", fontsize=9, color="#222222")
ax.annotate("one Gaussian (ML fit):\none broad bump", xy=(1.23, 0.232),
            xytext=(1.55, 0.345), fontsize=9, color="#8a8a8a",
            arrowprops=dict(arrowstyle="->", color="#8a8a8a", lw=1.0))

ax.set_xlim(-4.5, 5.5)
ax.set_ylim(0, 0.46)
ax.set_xlabel("feature $x$")
ax.set_ylabel("density")
ax.set_title("A mixture density is a weighted sum of bumps", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0.02, 1.0))
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-mixture-1d-components.png", dpi=200)
print("saved assets/figures/lec02-mixture-1d-components.png")
print("component peaks", round(P1 * g1.max(), 4), round(P2 * g2.max(), 4))
print("mixture peak height", round(float(mix.max()), 4), "at x =", round(float(x[mix.argmax()]), 3))
print("single Gaussian fit mean, sd", round(mu_hat, 4), round(np.sqrt(var_hat), 4))
