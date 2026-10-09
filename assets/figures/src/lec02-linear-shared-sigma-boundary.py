"""Figure code: lec02-linear-shared-sigma-boundary.

Shared covariance Sigma = sigma^2 I with sigma^2 = 1.
Means mu1 = [0, 0], mu2 = [4, 0].
Equal priors: the boundary is x1 = 2 (the midpoint of the means).
Priors 4:1: the boundary moves to x1 = 2 + sigma^2 ln(4)/||mu1-mu2|| = 2.3466,
that is toward omega_2, the class with the smaller prior.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2, red, gray = "#6a9fd6", "#d97757", "#dc2626", "#555555"


def ellipse(ax, mu, Sigma, c, **kw):
    vals, vecs = np.linalg.eigh(Sigma)
    t = np.linspace(0.0, 2.0 * np.pi, 400)
    pts = vecs @ np.diag(np.sqrt(vals) * c) @ np.vstack([np.cos(t), np.sin(t)])
    ax.plot(mu[0] + pts[0], mu[1] + pts[1], **kw)


mu1 = np.array([0.0, 0.0])
mu2 = np.array([4.0, 0.0])
s2 = 1.0
S = s2 * np.eye(2)
w = mu1 - mu2
mid = 0.5 * (mu1 + mu2)
x0_prior = mid - s2 * np.log(4.0) / float(w @ w) * w
shift = float(x0_prior[0] - mid[0])

fig, ax = plt.subplots(figsize=(7.8, 5.6))

for mu, col, lab in [(mu1, c1, r"$\mu_1$"), (mu2, c2, r"$\mu_2$")]:
    for c in (1.0, 2.0, 3.0):
        ellipse(ax, mu, S, c, color=col, lw=0.9, alpha=0.55)
    ax.scatter(*mu, color=col, s=100, zorder=6, edgecolor="white", linewidth=0.8)
    ax.annotate(lab, mu, xytext=(9, 9), textcoords="offset points", color=col, fontsize=13)

ax.axvline(mid[0], color=gray, ls="--", lw=1.8)
ax.axvline(x0_prior[0], color=red, ls="-", lw=2.4)

ybar = -3.0
ax.annotate("", xy=(mid[0], ybar), xytext=(x0_prior[0], ybar),
            arrowprops=dict(arrowstyle="<->", color=red, lw=1.6, shrinkA=0, shrinkB=0))
ax.text(mid[0] + 0.9, ybar - 0.15,
        f"shift {shift:.4f}", color=red, ha="left", fontsize=10)

ax.annotate("", xy=mu2, xytext=mu1,
            arrowprops=dict(arrowstyle="<->", color=c1, lw=1.4, ls=(0, (4, 3))))
ax.text(3.0, -0.5, r"$\mu_1-\mu_2$", color=c1, ha="center", fontsize=11)

ax.text(1.94, 2.4, "equal priors\n" + r"$x_1=2$", color=gray, ha="right", fontsize=9.5)
ax.text(3.62, 2.4, "priors 4:1\n" + r"$x_1=2.3466$", color=red, ha="center", fontsize=9.5)

ax.set_xlim(-1.6, 5.6)
ax.set_ylim(-3.6, 3.6)
ax.set_aspect("equal")
ax.set_xlabel(r"feature $x_1$")
ax.set_ylabel(r"feature $x_2$")
ax.set_title(r"Shared $\Sigma=\sigma^2 I$: the boundary is a straight line", fontsize=11)
ax.grid(alpha=0.25)
fig.text(0.5, 0.015, "Quadratic terms cancel, but $\\Sigma$ still sets where the line sits",
         ha="center", fontsize=9.5, color="#333333")
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig("assets/figures/lec02-linear-shared-sigma-boundary.png", dpi=200)
print("shift", round(shift, 4), "boundary", round(float(x0_prior[0]), 4))
