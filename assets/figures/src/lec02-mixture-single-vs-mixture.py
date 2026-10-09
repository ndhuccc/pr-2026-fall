"""Figure code: lec02-mixture-single-vs-mixture.

The 100-point data set (seed 3261) is a two-component Gaussian mixture in 2-D:
80% N((1,1), 0.10 I) and 20% N((2,2), 0.10 I). Left: the maximum-likelihood single
Gaussian cannot cover both clouds. Right: the two-component mixture does.
All contours are drawn from the fitted parameters, not hand-drawn.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def logpdf(X, mu, s2):
    d2 = np.sum((X - mu) ** 2, axis=1)
    return -np.log(2 * np.pi * s2) - d2 / (2 * s2)


def em(X, mu, s2, P, iters=60):
    for _ in range(iters):
        logp = np.stack([np.log(P[j]) + logpdf(X, mu[j], s2[j]) for j in range(2)], axis=1)
        m = logp.max(axis=1, keepdims=True)
        w = np.exp(logp - m)
        g = w / w.sum(axis=1, keepdims=True)
        Nk = g.sum(axis=0)
        mu = (g.T @ X) / Nk[:, None]
        s2 = np.array([np.sum(g[:, j] * np.sum((X - mu[j]) ** 2, axis=1)) / (2 * Nk[j])
                       for j in range(2)])
        P = Nk / X.shape[0]
    return mu, s2, P


rng = np.random.default_rng(seed=3261)
z = rng.random(100) < 0.8
X = np.empty((100, 2))
X[z] = rng.normal([1.0, 1.0], 0.10 ** 0.5, size=(int(z.sum()), 2))
X[~z] = rng.normal([2.0, 2.0], 0.10 ** 0.5, size=(int((~z).sum()), 2))

# single-Gaussian ML fit
mu_s = X.mean(axis=0)
Cov_s = (X - mu_s).T @ (X - mu_s) / X.shape[0]
ev, evec = np.linalg.eigh(Cov_s)
ang_s = np.degrees(np.arctan2(evec[1, -1], evec[0, -1]))

# mixture EM fit
mu_m, s2_m, P_m = em(X, np.array([[1.37, 1.20], [1.81, 1.62]]),
                     np.array([0.10, 0.10]), np.array([0.50, 0.50]))

fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), sharex=True, sharey=True)
lim = (0.0, 3.0)

ax = axes[0]
ax.scatter(X[:, 0], X[:, 1], s=16, color="#555555", alpha=0.7, linewidths=0)
for k in (1, 2):
    ax.add_patch(Ellipse(mu_s, 2 * k * np.sqrt(ev[1]), 2 * k * np.sqrt(ev[0]),
                         angle=ang_s, fill=False, edgecolor=c2,
                         lw=2.0 if k == 2 else 1.2, ls="-" if k == 2 else ":"))
ax.plot(mu_s[0], mu_s[1], marker="x", color=c2, ms=10, mew=2.2)
ax.text(0.04, 2.72, "one Gaussian:\none huge blob", fontsize=9.5, color=c2)
ax.set_title("(a) single Gaussian (ML)", fontsize=10)

ax = axes[1]
logp = np.stack([np.log(P_m[j]) + logpdf(X, mu_m[j], s2_m[j]) for j in range(2)], axis=1)
m = logp.max(axis=1, keepdims=True)
w = np.exp(logp - m)
g = w / w.sum(axis=1, keepdims=True)
sc = ax.scatter(X[:, 0], X[:, 1], c=g[:, 0], cmap="coolwarm", vmin=0, vmax=1,
                s=16, linewidths=0)
for j, col in enumerate((c1, c2)):
    ax.add_patch(Ellipse(mu_m[j], 4 * np.sqrt(s2_m[j]), 4 * np.sqrt(s2_m[j]),
                         angle=0, fill=False, edgecolor=col, lw=1.8, ls=":"))
    ax.plot(mu_m[j, 0], mu_m[j, 1], marker="x", color=col, ms=10, mew=2.2)
ax.text(0.04, 2.72, "two components:\ntight ellipses", fontsize=9.5, color="#333333")
ax.set_title("(b) two-component mixture (EM)", fontsize=10)
fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.03, label=r"$P(1\mid\mathbf{x})$")

for ax in axes:
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("$x_2$")

fig.tight_layout()
fig.savefig("assets/figures/lec02-mixture-single-vs-mixture.png", dpi=200)
print("saved assets/figures/lec02-mixture-single-vs-mixture.png")
print("single Gaussian mean", mu_s.round(4), "eig std", np.sqrt(ev).round(4))
print("single 2-sigma axes", (2 * np.sqrt(ev)).round(4), "angle", round(ang_s, 2))
print("mixture mu", mu_m.round(4), "s2", s2_m.round(5), "P", P_m.round(4))
print("mixture 2-sigma radii", (2 * np.sqrt(s2_m)).round(4))
print("points with P(1|x)>0.5 :", int((g[:, 0] > 0.5).sum()))
