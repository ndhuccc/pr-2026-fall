"""Figure code: lec02-predictive-widening. The predictive density is wider than the
plug-in density, by the extra term sigma_N^2.

Setting (same as lec02-posterior-sharpening): sigma^2 = 1, prior N(0, 10), x-bar = 2.
The predictive density is p(x|X) ~ N(mu_N, sigma^2 + sigma_N^2).
All numbers are computed from the formulas.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"

mu0, s0sq, s2 = 0.0, 10.0, 1.0
xbar = 2.0
N = 2

denom = N * s0sq + s2
muN = (N * s0sq * xbar + s2 * mu0) / denom
sNsq = (s2 * s0sq) / denom
pred_var = s2 + sNsq


def gauss(x, m, var):
    return np.exp(-(x - m) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)


x = np.linspace(-6, 10, 800)
post = gauss(x, muN, sNsq)
plug = gauss(x, muN, s2)
pred = gauss(x, muN, pred_var)

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4))

ax = axes[0]
plug_peak = 1.0 / np.sqrt(2 * np.pi * s2)
pred_peak = 1.0 / np.sqrt(2 * np.pi * pred_var)
post_peak = 1.0 / np.sqrt(2 * np.pi * sNsq)
ax.fill_between(x, plug, pred, color="#9a7fd0", alpha=0.35,
                label=r"extra $\sigma_N^2$ uncertainty")
ax.plot(x, plug, color="#6a9fd6", lw=2.0,
        label=rf"plug-in $\mathcal{{N}}(\mu_N,\sigma^2)$, peak {plug_peak:.4f}")
ax.plot(x, pred, color="#6a4c9c", lw=2.2,
        label=rf"predictive $\mathcal{{N}}(\mu_N,\sigma^2+\sigma_N^2)$, peak {pred_peak:.4f}")
ax.plot(x, post, color="#999999", ls="--", lw=1.5,
        label=rf"posterior $p(\mu\mid X)$, peak {post_peak:.4f}")
ax.annotate(r"predictive is wider by $\sigma_N^2$", xy=(muN + 1.55, 0.13),
            xytext=(muN + 2.2, 0.30), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#333333", lw=1.0))
ax.set_xlim(-6, 10)
ax.set_ylim(0, 0.70)
ax.set_xlabel("new sample $x$")
ax.set_ylabel("density")
ax.set_title(rf"(a) $N={N}$: predictive vs plug-in", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.grid(alpha=0.3)

ax = axes[1]
ns = np.arange(1, 21)
pred_sd = np.sqrt(s2 + (s2 * s0sq) / (ns * s0sq + s2))
ax.plot(ns, pred_sd, color="#6a4c9c", lw=2.2, marker="o", ms=3.5,
        label=r"predictive sd $\sqrt{\sigma^2+\sigma_N^2}$")
ax.axhline(np.sqrt(s2), color="#6a9fd6", ls="--", lw=1.6,
           label=r"plug-in sd $\sigma$")
ax.annotate(rf"$N={N}$: pred. sd $= {np.sqrt(pred_var):.4f}$",
            xy=(N, np.sqrt(pred_var)), xytext=(4.2, 1.44), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#333333", lw=1.0))
ax.annotate(rf"$N=20$: pred. sd $= {np.sqrt(s2 + (s2 * s0sq) / (20 * s0sq + s2)):.4f}$",
            xy=(20, np.sqrt(s2 + (s2 * s0sq) / (20 * s0sq + s2))),
            xytext=(8.0, 1.10), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#333333", lw=1.0))
ax.set_xlim(1, 20)
ax.set_ylim(0.95, 1.55)
ax.set_xlabel("number of samples $N$")
ax.set_ylabel("standard deviation of $x$")
ax.set_title("(b) extra uncertainty fades as $N$ grows", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="upper right")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-predictive-widening.png", dpi=200)
print("saved assets/figures/lec02-predictive-widening.png")
print(f"muN={muN:.4f} sigma_N^2={sNsq:.4f} pred_var={pred_var:.4f} "
      f"pred_sd={np.sqrt(pred_var):.4f}")
print(f"plug peak={plug.max():.4f} pred peak={pred.max():.4f} "
      f"posterior peak={post.max():.4f}")
for n in (1, 2, 5, 10, 20):
    print(f"N={n:3d} pred_sd={np.sqrt(s2 + (s2 * s0sq) / (n * s0sq + s2)):.4f}")
