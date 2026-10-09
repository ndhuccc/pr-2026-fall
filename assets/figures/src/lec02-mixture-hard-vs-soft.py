"""Figure code: lec02-mixture-hard-vs-soft.

The same 100 points (seed 3261), the same starting centres, two algorithms.
Left: k-means updates centres from a hard nearest-centre assignment, so every
point belongs to exactly one cluster (two solid colours).
Right: EM keeps a soft responsibility P(1|x), so points near the middle carry
weight in both components (continuous colour).
The one ambiguous point (responsibility closest to 0.5 under EM) is ringed to
show what the hard rule has to decide with no confidence measure.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def logpdf(X, mu, s2):
    d2 = np.sum((X - mu) ** 2, axis=1)
    return -np.log(2 * np.pi * s2) - d2 / (2 * s2)


def kmeans(X, mu, iters=100):
    for _ in range(iters):
        d = np.stack([np.sum((X - m) ** 2, axis=1) for m in mu], axis=1)
        lab = d.argmin(axis=1)
        new = np.stack([X[lab == j].mean(axis=0) for j in range(2)])
        if np.allclose(new, mu):
            break
        mu = new
    return mu, lab


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
    return mu, s2, P, g


rng = np.random.default_rng(seed=3261)
z = rng.random(100) < 0.8
X = np.empty((100, 2))
X[z] = rng.normal([1.0, 1.0], 0.10 ** 0.5, size=(int(z.sum()), 2))
X[~z] = rng.normal([2.0, 2.0], 0.10 ** 0.5, size=(int((~z).sum()), 2))

mu0 = np.array([[1.37, 1.20], [1.81, 1.62]])
km_mu, km_lab = kmeans(X, mu0.copy())
em_mu, em_s2, em_P, g = em(X, mu0.copy(), np.array([0.10, 0.10]), np.array([0.50, 0.50]))

amb = int(np.argmin(np.abs(g[:, 0] - 0.5)))

fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2), sharex=True, sharey=True)
lim = (0.0, 3.0)

ax = axes[0]
ax.scatter(X[km_lab == 0, 0], X[km_lab == 0, 1], s=20, color=c1, linewidths=0)
ax.scatter(X[km_lab == 1, 0], X[km_lab == 1, 1], s=20, color=c2, linewidths=0)
ax.scatter(X[amb, 0], X[amb, 1], s=210, facecolors="none", edgecolors="#111111",
           linewidths=1.6, zorder=6)
for m, col in zip(km_mu, (c1, c2)):
    ax.plot(m[0], m[1], marker="x", color=col, ms=10, mew=2.2)
ax.set_title("(a) k-means: hard ownership", fontsize=10)
ax.text(0.04, 2.72, "weight 0 or 1,\nno confidence", fontsize=9.5, color="#333333")

ax = axes[1]
sc = ax.scatter(X[:, 0], X[:, 1], c=g[:, 0], cmap="coolwarm", vmin=0, vmax=1,
                 s=20, linewidths=0)
ax.scatter(X[amb, 0], X[amb, 1], s=210, facecolors="none", edgecolors="#111111",
           linewidths=1.6, zorder=6)
for m, col in zip(em_mu, (c1, c2)):
    ax.plot(m[0], m[1], marker="x", color=col, ms=10, mew=2.2)
ax.annotate(f"$P(1\\mid\\mathbf{{x}})={g[amb,0]:.3f}$", (X[amb, 0], X[amb, 1]),
            textcoords="offset points", xytext=(-6, -30), fontsize=9, color="#111111",
            ha="right", arrowprops=dict(arrowstyle="->", color="#111111", lw=1.0))
ax.set_title("(b) EM: soft responsibility", fontsize=10)
ax.text(0.04, 2.72, "weight between 0 and 1", fontsize=9.5, color="#333333")
fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.03, label=r"$P(1\mid\mathbf{x})$")

for ax in axes:
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_aspect("equal")
    ax.set_xlabel("$x_1$")
    ax.grid(alpha=0.3)
axes[0].set_ylabel("$x_2$")

fig.tight_layout()
fig.savefig("assets/figures/lec02-mixture-hard-vs-soft.png", dpi=200)
print("saved assets/figures/lec02-mixture-hard-vs-soft.png")
print("k-means centres", km_mu.round(4).tolist(), "cluster sizes",
      int((km_lab == 0).sum()), int((km_lab == 1).sum()))
print("EM centres", em_mu.round(4).tolist(), "P", em_P.round(4).tolist())
print("ambiguous point", X[amb].round(4).tolist(), "r1 =", round(float(g[amb, 0]), 4))
print("EM effective weights N1, N2", (g.sum(axis=0)).round(4).tolist())
