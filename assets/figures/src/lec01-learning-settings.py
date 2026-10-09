"""Figure code: lec01-learning-settings. The same simulated points under three learning settings.

Panel (a) supervised: every point has a label and a decision line is drawn.
Panel (b) unsupervised: the same points, no labels.
Panel (c) semi-supervised: only four anchor points keep their labels.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
rng = np.random.default_rng(3)
X1 = rng.normal([1.0, 1.0], 0.45, size=(12, 2))   # group 1 (simulated)
X2 = rng.normal([2.6, 2.4], 0.45, size=(12, 2))   # group 2 (simulated)
X = np.vstack([X1, X2])
y = np.array([0] * 12 + [1] * 12)

m1, m2 = X1.mean(axis=0), X2.mean(axis=0)
w = m2 - m1
mid = (m1 + m2) / 2
t = np.linspace(0, 4, 100)
d = np.array([-w[1], w[0]]) / np.linalg.norm(w)
boundary = mid + np.outer(t - 2, d / d[0])

anchors = [0, 1, 12, 13]          # four labelled points for panel (c)
gray, c0, c1 = "#9a9a9a", "#6a9fd6", "#d97757"

fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.9), sharex=True, sharey=True)

ax = axes[0]
ax.scatter(X[y == 0, 0], X[y == 0, 1], color=c0, marker="o", label="class A")
ax.scatter(X[y == 1, 0], X[y == 1, 1], color=c1, marker="x", label="class B")
ax.plot(boundary[:, 0], boundary[:, 1], color="#333333", lw=1.4)
ax.set_title("(a) supervised: all labels known", fontsize=10)

ax = axes[1]
ax.scatter(X[:, 0], X[:, 1], color=gray, marker="o")
ax.set_title("(b) unsupervised: no labels", fontsize=10)

ax = axes[2]
ax.scatter(X[:, 0], X[:, 1], color=gray, marker="o", alpha=0.7)
for i in anchors:
    color = c0 if y[i] == 0 else c1
    marker = "o" if y[i] == 0 else "x"
    ax.scatter(X[i, 0], X[i, 1], color=color, marker=marker, s=70, zorder=4)
ax.set_title("(c) semi-supervised: 4 labels", fontsize=10)

for ax in axes:
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x_1$")
    ax.grid(alpha=0.3)
axes[0].set_ylabel(r"$x_2$")
axes[0].legend(loc="upper left", frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("assets/figures/lec01-learning-settings.png", dpi=200)
print("saved assets/figures/lec01-learning-settings.png")
