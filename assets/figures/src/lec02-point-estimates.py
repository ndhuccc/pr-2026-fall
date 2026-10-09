"""Figure code: lec02-point-estimates. Posterior vs the ML and MAP point estimates,
for small N and large N.

Setting (same as lec02-posterior-sharpening): sigma^2 = 1, prior N(0, 10), x-bar = 2.
The ML estimate is x-bar = 2. The MAP estimate is the posterior mode, mu_N.
All numbers are computed from the formulas.
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


fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.9))

setups = [(2, (0.6, 3.4), 0.95), (20, (1.4, 2.6), 2.4)]
for ax, (n, xr, ymax) in zip(axes, setups):
    m, v = post_params(n)
    x = np.linspace(*xr, 800)
    ax.plot(x, gauss(x, m, v), color="#6a4c9c", lw=2.4,
            label=rf"posterior $p(\mu\mid X)$, $N={n}$")
    ax.axvline(xbar, color="#6a9fd6", ls="--", lw=1.6,
               label=rf"ML estimate $={xbar:.3f}$")
    ax.axvline(m, color="#d97757", ls="-.", lw=1.6,
               label=rf"MAP estimate $={m:.3f}$")
    ax.set_xlim(*xr)
    ax.set_ylim(0, ymax)
    ax.set_xlabel(r"parameter $\mu$")
    ax.set_ylabel(r"density")
    ax.set_title(rf"({'a' if n == 2 else 'b'}) $N={n}$", fontsize=10)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    ax.grid(alpha=0.3)

axes[0].text(2.15, 0.80, "ML and MAP\ndiffer a little", fontsize=9, color="#333333")
axes[1].text(1.44, 1.35, "ML and MAP\nnearly coincide", fontsize=9, color="#333333")

fig.suptitle("Posterior, ML spike, and MAP spike", fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig("assets/figures/lec02-point-estimates.png", dpi=200)
print("saved assets/figures/lec02-point-estimates.png")
for n in (2, 20):
    m, v = post_params(n)
    print(f"N={n:3d} ML={xbar:.4f} MAP={m:.4f} gap={abs(xbar - m):.4f} sigma_N^2={v:.4f}")
