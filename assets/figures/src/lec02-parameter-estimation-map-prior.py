"""Figure code: lec02-parameter-estimation-map-prior.

Why a flat prior lets MAP collapse to ML, while a sharp prior does not.
The same five samples are used as in the ML peak figure, so xbar = 2.5.
Curves are the prior p(mu) and the likelihood, each scaled to peak 1.
MAP for N = 5, mu0 = -2.0, sigma^2 = 1.0.
  (a) sigma_mu^2 = 100 -> MAP = 2.4911, posterior sd 0.4468
  (b) sigma_mu^2 = 0.05 -> MAP = -1.1000, posterior sd 0.2000
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"

mu0, s2 = -2.0, 1.0
xbar = 2.5
n = 5

mu = np.linspace(-4.0, 4.0, 800)
like = np.exp(-n * (mu - xbar) ** 2 / (2 * s2))
like /= like.max()

fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))

for ax, smu2 in zip(axes, (100.0, 0.05)):
    prior = np.exp(-(mu - mu0) ** 2 / (2 * smu2))
    prior /= prior.max()
    w = smu2 / s2 * n
    mapv = (mu0 + w * xbar) / (1 + w)
    post_var = 1.0 / (1.0 / smu2 + n / s2)

    ax.plot(mu, prior, color=c1, lw=2.0, ls="--", label=r"prior $p(\mu)$")
    ax.plot(mu, like, color=c2, lw=2.2, label=r"likelihood $p(X\mid\mu)$")
    ax.axvline(mu0, color=c1, ls=":", lw=1.2)
    ax.axvline(xbar, color=c2, ls=":", lw=1.2)
    ax.axvline(mapv, color="#333333", lw=2.0)
    ax.plot([mapv], [0.06], "*", color="#333333", ms=13, zorder=5)
    ax.annotate(r"$\hat{\mu}_{MAP}$" f" $= {mapv:.4f}$", (mapv, 0.06),
                textcoords="offset points", xytext=(8, 12), fontsize=9)
    ax.text(0.03, 0.20, r"$\mu_0=-2.0$", transform=ax.transAxes, fontsize=9, color=c1)
    ax.text(0.03, 0.11, r"$\bar{x}=\hat{\mu}_{ML}=2.5$", transform=ax.transAxes,
            fontsize=9, color=c2)
    ax.set_xlabel(r"value of $\mu$")
    ax.set_ylabel("density, scaled to peak 1")
    ax.set_title(rf"(a) flat prior $\sigma_\mu^2={smu2:g}$" if smu2 > 1
                 else rf"(b) sharp prior $\sigma_\mu^2={smu2:g}$", fontsize=10)
    ax.text(0.97, 0.94, rf"posterior sd $= {post_var ** 0.5:.4f}$",
            transform=ax.transAxes, fontsize=9, ha="right")
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 1.08)
    ax.legend(frameon=False, fontsize=9, loc="center left", bbox_to_anchor=(0.0, 0.45))
    ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-parameter-estimation-map-prior.png", dpi=200)
print("saved assets/figures/lec02-parameter-estimation-map-prior.png")
for smu2 in (100.0, 0.05):
    w = smu2 / s2 * n
    print("smu2", smu2, "MAP", round((mu0 + w * xbar) / (1 + w), 4),
          "post sd", round((1.0 / (1.0 / smu2 + n / s2)) ** 0.5, 4),
          "frac", round(w / (1 + w), 4))
