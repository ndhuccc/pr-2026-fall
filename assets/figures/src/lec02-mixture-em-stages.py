"""Figure code: lec02-mixture-em-stages.

Three snapshots of the same 100-point mixture data (seed 3261) during EM:
iteration 0, 2 and 10. Every point is coloured by its E-step responsibility
P(1|x), and the two component ellipses (2 sigma) are drawn from the parameters
of that iteration. Nothing is hand-placed; all quantities come from the formulas.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def logpdf(X, mu, s2):
    d2 = np.sum((X - mu) ** 2, axis=1)
    return -np.log(2 * np.pi * s2) - d2 / (2 * s2)


def em_snapshots(X, mu, s2, P, wanted, iters=60):
    snaps = {}
    for t in range(iters + 1):
        logp = np.stack([np.log(P[j]) + logpdf(X, mu[j], s2[j]) for j in range(2)], axis=1)
        m = logp.max(axis=1, keepdims=True)
        w = np.exp(logp - m)
        g = w / w.sum(axis=1, keepdims=True)
        if t in wanted:
            snaps[t] = (mu.copy(), s2.copy(), P.copy(), g.copy())
        if t == iters:
            break
        Nk = g.sum(axis=0)
        mu = (g.T @ X) / Nk[:, None]
        s2 = np.array([np.sum(g[:, j] * np.sum((X - mu[j]) ** 2, axis=1)) / (2 * Nk[j])
                       for j in range(2)])
        P = Nk / X.shape[0]
    return snaps


rng = np.random.default_rng(seed=3261)
z = rng.random(100) < 0.8
X = np.empty((100, 2))
X[z] = rng.normal([1.0, 1.0], 0.10 ** 0.5, size=(int(z.sum()), 2))
X[~z] = rng.normal([2.0, 2.0], 0.10 ** 0.5, size=(int((~z).sum()), 2))

snaps = em_snapshots(X, np.array([[1.37, 1.20], [1.81, 1.62]]),
                     np.array([0.10, 0.10]), np.array([0.50, 0.50]), wanted={0, 2, 10})

fig, axes = plt.subplots(1, 3, figsize=(12.4, 4.6), sharex=True, sharey=True)
lim = (0.0, 3.0)
for ax, t in zip(axes, (0, 2, 10)):
    mu, s2, P, g = snaps[t]
    sc = ax.scatter(X[:, 0], X[:, 1], c=g[:, 0], cmap="coolwarm", vmin=0, vmax=1,
                     s=16, linewidths=0)
    for j, col in enumerate((c1, c2)):
        ax.add_patch(Ellipse(mu[j], 4 * np.sqrt(s2[j]), 4 * np.sqrt(s2[j]),
                             fill=False, edgecolor=col, lw=1.8, ls=":"))
        ax.plot(mu[j, 0], mu[j, 1], marker="x", color=col, ms=9, mew=2.2)
    ax.set_title(f"iteration {t}", fontsize=10)
    bb = dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.7)
    ax.text(0.03, 0.045,
            f"$P_1$={P[0]:.3f}\n$\\mu_1$=({mu[0,0]:.2f},{mu[0,1]:.2f})",
            transform=ax.transAxes, fontsize=8.0, color=c1, va="bottom", bbox=bb)
    ax.text(0.55, 0.045,
            f"$P_2$={P[1]:.3f}\n$\\mu_2$=({mu[1,0]:.2f},{mu[1,1]:.2f})",
            transform=ax.transAxes, fontsize=8.0, color=c2, va="bottom", bbox=bb)
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("$x_2$")
fig.colorbar(sc, ax=axes, fraction=0.035, pad=0.02, label=r"$P(1\mid\mathbf{x})$")
fig.savefig("assets/figures/lec02-mixture-em-stages.png", dpi=200, bbox_inches="tight")
print("saved assets/figures/lec02-mixture-em-stages.png")
for t in (0, 2, 10):
    mu, s2, P, g = snaps[t]
    print(t, "P", P.round(4), "mu", mu.round(3).tolist(),
          "2sigma radii", (2 * np.sqrt(s2)).round(4).tolist(),
          "hard count", int((g[:, 0] > 0.5).sum()), int((g[:, 0] < 0.5).sum()),
          "ambiguous", int(((g[:, 0] >= 0.05) & (g[:, 0] <= 0.95)).sum()))
