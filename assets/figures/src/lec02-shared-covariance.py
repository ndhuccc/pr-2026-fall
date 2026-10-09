"""Figure code: lec02-shared-covariance. Preview: a shared covariance makes the boundary a straight line.

The numbers are the ones already used in the lecture (Section 5.3): mu1 = 0 with sigma^2 = 1,
and mu2 = 2 with sigma^2 = 4. Here they are extended to two features so that the "line or
hyperplane" wording of Section 6 can be shown:
  (a) shared covariance, Sigma_1 = Sigma_2 = I  -> the boundary is the straight line x1 = 1;
  (b) different covariances, Sigma_1 = I and Sigma_2 = diag(4, 1) -> the boundary bends, and it
      crosses the horizontal axis at x1 = -2.571 and x1 = 1.238, the same two points as in 1-D.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"
mu1 = np.array([0.0, 0.0])
mu2 = np.array([2.0, 0.0])


def g(x1, x2, mu, S):
    d = np.stack([x1 - mu[0], x2 - mu[1]], axis=-1)
    Si = np.linalg.inv(S)
    quad = np.einsum("...i,ij,...j->...", d, Si, d)
    return -0.5 * quad - 0.5 * np.log(np.linalg.det(S))


X1, X2 = np.meshgrid(np.linspace(-4.5, 6.0, 700), np.linspace(-3.2, 3.2, 560))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.3))

# (a) shared covariance: boundary is a straight line
S = np.eye(2)
Z = g(X1, X2, mu1, S) - g(X1, X2, mu2, S)
ax1.contourf(X1, X2, np.where(Z > 0, 1, 0), levels=[-0.5, 0.5, 1.5], colors=[c2, c1], alpha=0.15)
ax1.contour(X1, X2, Z, levels=[0], colors="#333333", linewidths=2.2)
ax1.plot([1, 1], [-3.2, 3.2], color="#e0995f", ls="--", lw=1.0)
ax1.text(1.15, 2.5, r"$x_1=1$", fontsize=10)
ax1.set_title("(a) shared $\\Sigma$: straight boundary", fontsize=10)

# (b) different covariances: boundary bends
S1, S2 = np.eye(2), np.diag([4.0, 1.0])
Z2 = g(X1, X2, mu1, S1) - g(X1, X2, mu2, S2)
ax2.contourf(X1, X2, np.where(Z2 > 0, 1, 0), levels=[-0.5, 0.5, 1.5], colors=[c2, c1], alpha=0.15)
ax2.contour(X1, X2, Z2, levels=[0], colors="#333333", linewidths=2.2)
for xc in (-2.571, 1.238):
    ax2.plot([xc, xc], [-3.2, 3.2], color="#e0995f", ls="--", lw=1.0)
ax2.text(-2.571, -2.75, r"$-2.571$", fontsize=9, ha="right", va="center")
ax2.text(1.238, -2.75, r"$1.238$", fontsize=9, ha="left", va="center")
ax2.set_title("(b) different $\\Sigma$: curved boundary", fontsize=10)

for ax in (ax1, ax2):
    ax.scatter([mu1[0], mu2[0]], [mu1[1], mu2[1]], color=[c1, c2], s=46, zorder=3)
    ax.annotate(r"$\mu_1$", (mu1[0], mu1[1]), textcoords="offset points", xytext=(-26, 12),
                fontsize=10, color=c1)
    ax.annotate(r"$\mu_2$", (mu2[0], mu2[1]), textcoords="offset points",
                xytext=(10, 12), fontsize=10, color=c2)
    ax.set_aspect("equal")
    ax.set_xlim(-4.5, 6.0)
    ax.set_ylim(-3.2, 3.2)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-shared-covariance.png", dpi=200)
print("saved assets/figures/lec02-shared-covariance.png")

# verify: axis intercepts of the curved boundary, and the straight boundary of panel (a)
xs = np.linspace(-6, 8, 2_000_001)
zs = g(xs, np.zeros_like(xs), mu1, S1) - g(xs, np.zeros_like(xs), mu2, S2)
crossings = xs[1:][np.sign(zs[1:]) != np.sign(zs[:-1])]
print("curved boundary x-intercepts", np.round(crossings, 3))
za = g(np.array([1.0]), np.array([0.0]), mu1, S) - g(np.array([1.0]), np.array([0.0]), mu2, S)
print("panel (a): g1-g2 at (1,0) =", np.round(za, 8), "(0 means the straight boundary passes through x1 = 1)")