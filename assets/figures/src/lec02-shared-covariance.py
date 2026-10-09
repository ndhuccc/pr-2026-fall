"""Figure code: lec02-shared-covariance. Preview: a shared covariance makes the boundary a line.

Illustrative two-class example (not from the textbook). Equal priors; means (-1, 0) and (+1, 0).
Left: Sigma_1 = Sigma_2 = I, the boundary is the straight line x1 = 0.
Right: different covariances, the boundary is a curve.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"
mu1 = np.array([-1.0, 0.0])
mu2 = np.array([1.0, 0.0])


def g(x1, x2, mu, S):
    d = np.stack([x1 - mu[0], x2 - mu[1]], axis=-1)
    Si = np.linalg.inv(S)
    quad = np.einsum("...i,ij,...j->...", d, Si, d)
    return -0.5 * quad - 0.5 * np.log(np.linalg.det(S))


X1, X2 = np.meshgrid(np.linspace(-4, 4, 500), np.linspace(-4, 4, 500))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.8))
cases = [
    (ax1, np.eye(2), np.eye(2), "(a) shared $\\Sigma$: straight boundary"),
    (ax2, np.eye(2), np.array([[2.0, 0.0], [0.0, 0.5]]), "(b) different $\\Sigma$: curved boundary"),
]
for ax, S1, S2, title in cases:
    Z = g(X1, X2, mu1, S1) - g(X1, X2, mu2, S2)
    ax.contourf(X1, X2, np.where(Z > 0, 1, 0), levels=[-0.5, 0.5, 1.5], colors=[c2, c1], alpha=0.15)
    ax.contour(X1, X2, Z, levels=[0], colors="#333333", linewidths=2.0)
    ax.scatter([mu1[0], mu2[0]], [mu1[1], mu2[1]], color=[c1, c2], s=44, zorder=3)
    ax.set_aspect("equal")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title(title, fontsize=10)
    ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-shared-covariance.png", dpi=200)
print("saved assets/figures/lec02-shared-covariance.png")
Z = g(np.array([0.0]), np.array([0.0]), mu1, np.eye(2)) - g(np.array([0.0]), np.array([0.0]), mu2, np.eye(2))
print("left boundary check: g1-g2 at (0,0) =", np.round(Z, 6))
