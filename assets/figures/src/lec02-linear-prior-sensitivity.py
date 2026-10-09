"""Figure code: lec02-linear-prior-sensitivity.

Two panels with the same means mu1 = [0, 0], mu2 = [4, 0].
Shared Sigma = sigma^2 I. Moving the priors from 1:1 to 4:1 moves the
boundary by sigma^2 ln(4)/||mu1-mu2||.
(a) tight classes, sigma^2 = 0.5  -> shift 0.1733
(b) spread classes, sigma^2 = 2.5 -> shift 0.8664
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2, red, gray = "#6a9fd6", "#d97757", "#dc2626", "#555555"

rng = np.random.default_rng(0)
mu1 = np.array([0.0, 0.0])
mu2 = np.array([4.0, 0.0])
w = mu1 - mu2
mid = 0.5 * (mu1 + mu2)

fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.0), sharey=True)

for ax, s2, tag in [(axes[0], 0.5, "(a) tight classes"), (axes[1], 2.5, "(b) spread classes")]:
    S = s2 * np.eye(2)
    shift = s2 * np.log(4.0) / float(w @ w) * abs(w[0])
    for mu, col in [(mu1, c1), (mu2, c2)]:
        pts = rng.multivariate_normal(mu, S, size=160)
        ax.scatter(pts[:, 0], pts[:, 1], s=7, color=col, alpha=0.35, rasterized=True)
        ax.scatter(*mu, color=col, s=80, zorder=6, edgecolor="white", linewidth=0.8)
    ax.axvline(mid[0], color=gray, ls="--", lw=1.8)
    ax.axvline(mid[0] + shift, color=red, ls="-", lw=2.4)
    ybar = -3.2
    ax.annotate("", xy=(mid[0], ybar), xytext=(mid[0] + shift, ybar),
                arrowprops=dict(arrowstyle="<->", color=red, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(mid[0] + shift + 0.15, ybar - 0.35, f"{shift:.4f}", color=red, ha="left", fontsize=10)
    ax.set_title(f"{tag}, " + r"$\sigma^2=" + f"{s2:g}$", fontsize=11)
    ax.set_xlim(-2.0, 6.0)
    ax.set_ylim(-4.0, 4.0)
    ax.set_aspect("equal")
    ax.set_xlabel(r"feature $x_1$")
    ax.grid(alpha=0.25)

axes[0].set_ylabel(r"feature $x_2$")
axes[0].text(-1.9, 3.1, "priors 1:1 (dashed)\npriors 4:1 (red)", fontsize=9.5, color="#333333")
fig.suptitle("Same prior change, different shift: the scale of $\\Sigma$ decides", fontsize=11.5)
print("tight shift", round(0.5 * np.log(4) / 4, 4), "spread shift", round(2.5 * np.log(4) / 4, 4))
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig("assets/figures/lec02-linear-prior-sensitivity.png", dpi=200)
