"""Figure code: lec02-gaussian-contours. Sigma sets the shape of equal-probability contours.

Illustrative covariance values (not from the textbook). Left: Sigma = I gives circles.
Right: a general Sigma gives ellipses whose axes follow the eigen-decomposition of Sigma.
Contours are drawn at Mahalanobis radius k (k = 1 and 2).
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1 = "#5fb8a8"
t = np.linspace(0, 2 * np.pi, 400)


def contour(Sigma, k):
    vals, vecs = np.linalg.eigh(Sigma)
    return vecs @ np.diag(np.sqrt(vals)) @ np.vstack([k * np.cos(t), k * np.sin(t)])


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.8))
for ax, Sigma, title in [
    (ax1, np.eye(2), r"(a) $\Sigma = I$: circles"),
    (ax2, np.array([[2.0, 1.2], [1.2, 1.0]]), r"(b) general $\Sigma$: ellipses"),
]:
    for k, alpha in [(1.0, 1.0), (2.0, 0.5)]:
        e = contour(Sigma, k)
        ax.plot(e[0], e[1], color=c1, lw=2.2, alpha=alpha)
    ax.scatter([0], [0], color="#d97757", zorder=3, s=36)
    ax.axhline(0, color="#b7b0a5", lw=0.8)
    ax.axvline(0, color="#b7b0a5", lw=0.8)
    ax.set_aspect("equal")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title(title, fontsize=10)
    ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-gaussian-contours.png", dpi=200)
print("saved assets/figures/lec02-gaussian-contours.png")
print("eig general", np.round(np.linalg.eigvalsh(np.array([[2.0, 1.2], [1.2, 1.0]])), 4))
