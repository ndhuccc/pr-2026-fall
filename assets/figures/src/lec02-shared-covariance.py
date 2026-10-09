"""Figure code: lec02-shared-covariance. Preview: shared vs different covariance.

Numbers come from the lecture's 1-D example (Section 5.3): mu1 = 0 and mu2 = 2, with variances 1 and 4.
Extended to two features:
  (a) shared covariance, Sigma_1 = Sigma_2 = I -> the boundary is the single straight line x1 = 1
      (right where the two means are equidistant);
  (b) different covariances, Sigma_1 = I and Sigma_2 = [[4, 0.5], [0.5, 1]] -> the quadratic terms no
      longer cancel and the boundary bends into a hyperbola, crossing the horizontal axis at
      x1 = -2.67 and x1 = 1.22. The diagonal entries 4 and 1 are the lecture's variances; the
      off-diagonal 0.5 is chosen only so that the curvature is visible.
Fills are opaque pre-blended tints (no alpha), so the figure renders the same everywhere.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
W1, W2, ORANGE, DARK = "#6a9fd6", "#d97757", "#e0995f", "#1c1712"


def tint(hex_color, weight=0.15):
    r, g, b = (int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    f = lambda v: int(round(v * weight + 255 * (1 - weight)))
    return "#%02x%02x%02x" % (f(r), f(g), f(b))


TINT1, TINT2 = tint(W1), tint(W2)
mu1 = np.array([0.0, 0.0])
mu2 = np.array([2.0, 0.0])
S1 = np.eye(2)
S2 = np.array([[4.0, 0.5], [0.5, 1.0]])


def g(x1, x2, mu, S):
    dv = np.stack([x1 - mu[0], x2 - mu[1]], axis=-1)
    quad = np.einsum("...i,ij,...j->...", dv, np.linalg.inv(S), dv)
    return -0.5 * quad - 0.5 * np.log(np.linalg.det(S))


def fill_regions(ax, X1, X2, Z):
    ax.contourf(X1, X2, np.where(Z > 0, 1.0, 0.0), levels=[0.5, 1.5], colors=[TINT1])
    ax.contourf(X1, X2, np.where(Z > 0, 0.0, 1.0), levels=[0.5, 1.5], colors=[TINT2])
    ax.contour(X1, X2, Z, levels=[0], colors=[DARK], linewidths=2.0)


X1, X2 = np.meshgrid(np.linspace(-4.5, 6.0, 300), np.linspace(-3.0, 3.0, 220))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.6, 4.2))
for ax in (ax1, ax2):
    ax.set_facecolor("white")
fig.patch.set_facecolor("white")

fill_regions(ax1, X1, X2, g(X1, X2, mu1, S1) - g(X1, X2, mu2, S1))
ax1.text(1.15, 2.3, r"$x_1=1$", fontsize=9, color=DARK)
ax1.set_title("(a) shared $\\Sigma$: straight boundary", fontsize=9, color=DARK)

Z2 = g(X1, X2, mu1, S1) - g(X1, X2, mu2, S2)
fill_regions(ax2, X1, X2, Z2)
xs = np.linspace(-4.5, 6.0, 4001)
z0 = g(xs, np.zeros_like(xs), mu1, S1) - g(xs, np.zeros_like(xs), mu2, S2)
roots = []
for i in range(1, len(xs)):
    if (z0[i] > 0) != (z0[i - 1] > 0):
        roots.append(float(xs[i - 1] + (xs[i] - xs[i - 1]) * abs(z0[i - 1]) / (abs(z0[i - 1]) + abs(z0[i]))))
for r in roots:
    ax2.plot([r, r], [-3, 3], color=ORANGE, ls="--", lw=0.8)
ax2.text(roots[0] - 0.2, -2.75, f"${roots[0]:.2f}$", fontsize=8, ha="right", va="center", color=DARK)
ax2.text(roots[1] + 0.2, -2.75, f"${roots[1]:.2f}$", fontsize=8, ha="left", va="center", color=DARK)
ax2.text(2.2, 1.5, "the boundary bends when\n$\\Sigma_2$ has an off-diagonal term", fontsize=8, color=DARK)
ax2.set_title("(b) different $\\Sigma$: curved boundary", fontsize=9, color=DARK)

for ax in (ax1, ax2):
    ax.scatter([mu1[0], mu2[0]], [mu1[1], mu2[1]], color=[W1, W2], s=34, zorder=3)
    ax.set_aspect("equal")
    ax.set_xlim(-4.5, 6.0)
    ax.set_ylim(-3.0, 3.0)
    ax.set_xlabel(r"$x_1$", fontsize=8, color=DARK)
    ax.set_ylabel(r"$x_2$", fontsize=8, color=DARK)
    ax.tick_params(labelsize=7, colors=DARK)
fig.tight_layout()
fig.savefig("assets/figures/lec02-shared-covariance.png", dpi=200)
print("saved assets/figures/lec02-shared-covariance.png")
print("x-crossings", [round(r, 3) for r in roots])