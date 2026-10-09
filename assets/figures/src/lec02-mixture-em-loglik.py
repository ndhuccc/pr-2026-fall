"""Figure code: lec02-mixture-em-loglik.

Log-likelihood of the 100-point two-component mixture (seed 3261) as the EM
iterations run. L(t) is computed from the analytic mixture density, so the curve
is monotone by construction of the algorithm. Iterations 0, 2 and 10 are marked.
"""
import json
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def logpdf(X, mu, s2):
    d2 = np.sum((X - mu) ** 2, axis=1)
    return -np.log(2 * np.pi * s2) - d2 / (2 * s2)


def em(X, mu, s2, P, iters=60):
    L = []
    for t in range(iters + 1):
        logp = np.stack([np.log(P[j]) + logpdf(X, mu[j], s2[j]) for j in range(2)], axis=1)
        m = logp.max(axis=1, keepdims=True)
        w = np.exp(logp - m)
        g = w / w.sum(axis=1, keepdims=True)
        L.append(float(np.sum(m[:, 0] + np.log(w.sum(axis=1)))))
        if t == iters:
            break
        Nk = g.sum(axis=0)
        mu = (g.T @ X) / Nk[:, None]
        s2 = np.array([np.sum(g[:, j] * np.sum((X - mu[j]) ** 2, axis=1)) / (2 * Nk[j])
                       for j in range(2)])
        P = Nk / X.shape[0]
    return np.array(L)


rng = np.random.default_rng(seed=3261)
z = rng.random(100) < 0.8
X = np.empty((100, 2))
X[z] = rng.normal([1.0, 1.0], 0.10 ** 0.5, size=(int(z.sum()), 2))
X[~z] = rng.normal([2.0, 2.0], 0.10 ** 0.5, size=(int((~z).sum()), 2))

L = em(X, np.array([[1.37, 1.20], [1.81, 1.62]]),
       np.array([0.10, 0.10]), np.array([0.50, 0.50]))

fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.4))

ax = axes[0]
ax.plot(np.arange(len(L)), L, color=c1, lw=2.2, marker="o", ms=3.5)
for t in (0, 2, 10):
    ax.plot(t, L[t], marker="o", ms=8, mfc="none", mec=c2, mew=2.0)
ax.annotate(f"iter 0\n{L[0]:.2f}", (0, L[0]), textcoords="offset points",
            xytext=(9, 12), fontsize=9, color=c2, ha="left")
ax.annotate(f"iter 2\n{L[2]:.2f}", (2, L[2]), textcoords="offset points",
            xytext=(10, -34), fontsize=9, color=c2, ha="left")
ax.annotate(f"iter 10\n{L[10]:.2f}", (10, L[10]), textcoords="offset points",
            xytext=(16, 6), fontsize=9, color=c2, ha="left")
ax.set_ylim(float(L[0]) - 10, float(L[0]) + 112)
ax.set_xlabel("iteration $t$")
ax.set_ylabel("log-likelihood $L(t)$")
ax.set_title("(a) full climb over 60 iterations", fontsize=10)
ax.set_xlim(-2.5, 61)
ax.grid(alpha=0.3)

ax = axes[1]
gain = np.diff(L[:13])
t = np.arange(1, 13)
bars = ax.bar(t, gain, color=c1, edgecolor="#333333", linewidth=0.6)
for ti, gi in zip(t, gain):
    ax.text(ti, gi + 0.9, f"{gi:.2f}", ha="center", va="bottom", fontsize=8.5,
            color="#333333")
ax.axhline(0, color="#666666", lw=1.0)
first = gain[0]
ax.annotate(f"first step:\n+{first:.2f}", (1, first), textcoords="offset points",
            xytext=(16, -4), fontsize=9, color=c2)
ax.set_xlim(0.3, 12.7)
ax.set_ylim(min(0, float(gain.min()) - 2), float(gain.max()) * 1.45 + 3)
ax.set_xlabel("iteration $t$")
ax.set_ylabel(r"gain $L(t)-L(t-1)$")
ax.set_title("(b) every E-M cycle adds a non-negative amount", fontsize=10)
ax.grid(axis="y", alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-mixture-em-loglik.png", dpi=200)
print("saved assets/figures/lec02-mixture-em-loglik.png")
for t in (0, 1, 2, 3, 4, 5, 10, 20, 40, 60):
    print(f"L({t}) = {L[t]:.6f}")
print("monotone:", bool(np.all(np.diff(L) >= -1e-9)))
print("jump 0->1:", round(float(L[1] - L[0]), 4), " total gain:", round(float(L[-1] - L[0]), 4))
print("gains 1..12:", np.round(np.diff(L[:13]), 4).tolist())
