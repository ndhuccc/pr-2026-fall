"""Figure code: lec02-predictive-mixture. The predictive density is a weighted sum
of p(x|theta) over all theta, with weights p(theta|X); approximating that integral
by Gauss-Hermite nodes gives back the predictive Gaussian.

Setting (same as lec02-posterior-sharpening): sigma^2 = 1, prior N(0, 10), x-bar = 2,
N = 2, so the posterior is N(1.9048, 0.4762) and the predictive is N(1.9048, 1.4762).
The nodes and weights come from the exact quadrature rule, not from hand.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"

mu0, s0sq, s2, xbar, N = 0.0, 10.0, 1.0, 2.0, 2

denom = N * s0sq + s2
muN = (N * s0sq * xbar + s2 * mu0) / denom
sNsq = (s2 * s0sq) / denom
pred_var = s2 + sNsq
sd = np.sqrt(sNsq)


def gauss(x, m, var):
    return np.exp(-(x - m) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)


x = np.linspace(-6, 10, 1200)

# Gauss-Hermite quadrature for a Gaussian-weight integral
nodes, weights = np.polynomial.hermite.hermgauss(15)
weights = weights / np.sqrt(np.pi)
mus = muN + sd * np.sqrt(2.0) * nodes
mix = sum(w * gauss(x, m, s2) for w, m in zip(weights, mus))
exact = gauss(x, muN, pred_var)
pred_peak = 1.0 / np.sqrt(2 * np.pi * pred_var)

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.3))

ax = axes[0]
for w, m in zip(weights, mus):
    ax.plot(x, w * gauss(x, m, s2), color="#bfa8dd", lw=1.1)
ax.plot(x, mix, color="#6a4c9c", lw=2.6,
        label=rf"weighted sum $\approx\mathcal{{N}}({muN:.4f},{pred_var:.4f})$")
ax.set_xlim(-6, 10)
ax.set_ylim(0, 0.42)
ax.set_xlabel("new sample $x$")
ax.set_ylabel("weighted density")
ax.set_title(rf"(a) fifteen components $p(x\mid\theta)$, $N={N}$", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper right")
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(x, mix, color="#6a4c9c", lw=2.4,
        label=rf"weighted sum, peak {pred_peak:.4f}")
ax.plot(x, exact, color="#d97757", ls="--", lw=2.0,
        label=rf"predictive integral, peak {pred_peak:.4f}")
ax.set_xlim(-6, 10)
ax.set_ylim(0, 0.42)
ax.set_xlabel("new sample $x$")
ax.set_ylabel("density")
ax.set_title("(b) the weighted sum matches the integral", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper right")
ax.grid(alpha=0.3)

fig.suptitle(r"$p(x\mid X)=\int p(x\mid\theta)\,p(\theta\mid X)\,d\theta$, discretized",
             fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig("assets/figures/lec02-predictive-mixture.png", dpi=200)
print("saved assets/figures/lec02-predictive-mixture.png")
print(f"muN={muN:.4f} sNsq={sNsq:.4f} pred_var={pred_var:.4f} sd={sd:.4f}")
print(f"sum peak={mix.max():.4f} integral peak={exact.max():.4f}")
print("weights sum", round(float(weights.sum()), 6))
print("mus", np.round(mus, 4))
