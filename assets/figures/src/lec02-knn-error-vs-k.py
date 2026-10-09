"""Figure code: lec02-knn-error-vs-k.

The U-shaped test error of the k-nearest-neighbour rule. Two interleaving
half-moons (a non-linearly separable problem) plus a few mislabelled noise
points. Small k follows the noise (high variance); large k smooths across the
interlocking tips (high bias); the error is smallest in between.

All errors are computed here with a plain kNN vote on a fixed training and
test set; nothing is hand-filled. Odd k from 1 to 41.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
C_A, C_B = "#6a9fd6", "#d97757"
RED = "#dc2626"

rng = np.random.default_rng(3)


def moons(n, noise=0.14):
    n1 = n // 2
    t1 = rng.uniform(0, np.pi, n1)
    t2 = rng.uniform(0, np.pi, n - n1)
    x1 = np.c_[np.cos(t1), np.sin(t1)]
    x2 = np.c_[1 - np.cos(t2), 0.5 - np.sin(t2)]
    X = np.vstack([x1, x2]) + rng.normal(0, noise, size=(n, 2))
    y = np.r_[np.zeros(n1, int), np.ones(n - n1, int)]
    return X, y


Xtr, ytr = moons(300)
Xte, yte = moons(400)
# plant 12 mislabelled training points inside the opposite moon
idx = rng.choice(len(Xtr), 12, replace=False)
ytr[idx] = 1 - ytr[idx]


def knn_error(k, Xtr, ytr, Xte, yte):
    d = np.linalg.norm(Xte[:, None, :] - Xtr[None, :, :], axis=2)
    nn = np.argsort(d, axis=1)[:, :k]
    votes = ytr[nn]
    pred = (votes.mean(axis=1) > 0.5).astype(int)
    return float((pred != yte).mean())


ks = np.arange(1, 42, 2)
err = np.array([knn_error(int(k), Xtr, ytr, Xte, yte) for k in ks])
kbest = int(ks[int(np.argmin(err))])

fig, ax = plt.subplots(figsize=(8.6, 4.6))
ax.plot(ks, err * 100, "-o", color=C_A, lw=2.0, ms=4.5)
ax.plot([1], [err[0] * 100], "o", ms=9, mfc=RED, mec=RED)
ax.plot([kbest], [err.min() * 100], "o", ms=9, mfc=RED, mec=RED)
ax.plot([41], [err[-1] * 100], "o", ms=9, mfc=RED, mec=RED)
ax.annotate("$k{=}1$\nhigh variance\n(follows the noise)",
            (1, err[0] * 100), textcoords="offset points", xytext=(14, 6),
            fontsize=8.5)
ax.annotate(f"$k{{=}}{kbest}$: lowest test error\n{err.min()*100:.2f}%",
            (kbest, err.min() * 100), textcoords="offset points",
            xytext=(6, 26), fontsize=9, color=RED,
            arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
ax.annotate("$k{=}41$\nhigh bias\n(crosses the interlocking tips)",
            (41, err[-1] * 100), textcoords="offset points", xytext=(-170, -38),
            fontsize=8.5,
            arrowprops=dict(arrowstyle="->", lw=0.9))
ax.text(20, err.max() * 100 * 0.98, "U-shape: increasing $k$ first helps\n"
        "(kills noise), then hurts (erases structure)",
        ha="center", fontsize=9, color="#333333")
ax.set_xlabel("number of neighbours $k$")
ax.set_ylabel("test error (%)")
ax.set_title("kNN test error against $k$: a U-shaped curve", fontsize=10)
ax.set_xticks(np.arange(1, 42, 4))
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-knn-error-vs-k.png", dpi=200)
print("saved lec02-knn-error-vs-k.png")
print("kbest", kbest, "minerr", round(err.min(), 4))
for k, e in zip(ks, err):
    print(int(k), round(e, 4))
