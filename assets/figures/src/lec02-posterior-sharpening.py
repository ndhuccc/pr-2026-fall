"""Figure code: lec02-posterior-sharpening. The posterior p(mu|X) gets sharper as N grows.

Setting: known variance sigma^2 = 1, Gaussian prior N(mu_0, sigma_0^2) = N(0, 10),
sample mean x-bar = 2. Exact posterior mean and variance:
    mu_N    = (N sigma_0^2 x-bar + sigma^2 mu_0) / (N sigma_0^2 + sigma^2)
    sigma_N^2 = sigma^2 sigma_0^2 / (N sigma_0^2 + sigma^2)
All numbers are computed with the formula, not typed in by hand.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"

mu0, s0sq, s2 = 0.0, 10.0, 1.0
xbar = 2.0


def post_params(n):
    denom = n * s0sq + s2
    return (n * s0sq * xbar + s2 * mu0) / denom, (s2 * s0sq) / denom


def gauss(x, m, var):
    return np.exp(-(x - m) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)


x = np.linspace(-8, 8, 800)
colors = {1: "#c8b6e2", 2: "#9a7fd0", 5: "#6a4c9c", 20: "#2e1a5b"}

fig, ax = plt.subplots(figsize=(8.6, 5.0))
ax.plot(x, gauss(x, mu0, s0sq), color="#999999", ls="--", lw=1.6,
        label=r"prior $N(0,10)$")

labels = []
for n in (1, 2, 5, 20):
    m, v = post_params(n)
    y = gauss(x, m, v)
    ax.plot(x, y, color=colors[n], lw=2.0,
            label=rf"$N={n}$: $\sigma_N^2={v:.3f}$")
    labels.append((n, m, v, y.max()))

ax.axvline(xbar, color="#d97757", ls="-.", lw=1.4)
ax.text(xbar + 0.2, 1.55, r"true mean $\mu^* = 2$", color="#d97757", fontsize=9)
ax.annotate("sharper as $N$ grows", xy=(2.45, 1.20), xytext=(3.6, 1.05),
            fontsize=9, arrowprops=dict(arrowstyle="->", color="#333333", lw=1.0))

ax.set_xlim(-8, 8)
ax.set_ylim(0, 1.95)
ax.set_xlabel(r"parameter $\mu$")
ax.set_ylabel(r"posterior density $p(\mu \mid X)$")
ax.set_title("Posterior concentrates on the data as $N$ grows", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper left")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-posterior-sharpening.png", dpi=200)
print("saved assets/figures/lec02-posterior-sharpening.png")
for n, m, v, pk in labels:
    print(f"N={n:3d} mu_N={m:.4f} sigma_N^2={v:.4f} sd={np.sqrt(v):.4f} peak={pk:.4f}")
