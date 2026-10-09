"""Figure code: lec02-linear-nondiagonal-direction.

Shared but non-diagonal covariance Sigma = [[2.0, 1.2], [1.2, 1.5]],
means mu1 = [0, 0], mu2 = [4, 0], equal priors.
w = Sigma^{-1}(mu1 - mu2) = (-3.8462, 3.0769); the boundary is
perpendicular to w and passes through the midpoint (2, 0),
with slope 1.25. The raw mean difference mu1 - mu2 is horizontal,
so the line is no longer perpendicular to it.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2, red, gray = "#6a9fd6", "#d97757", "#dc2626", "#555555"


def ellipse(ax, mu, Sinv, c, **kw):
    vals, vecs = np.linalg.eigh(Sinv)
    t = np.linspace(0.0, 2.0 * np.pi, 400)
    pts = vecs @ np.diag(c / np.sqrt(vals)) @ np.vstack([np.cos(t), np.sin(t)])
    ax.plot(mu[0] + pts[0], mu[1] + pts[1], **kw)


mu1 = np.array([0.0, 0.0])
mu2 = np.array([4.0, 0.0])
Sigma = np.array([[2.0, 1.2], [1.2, 1.5]])
Sinv = np.linalg.inv(Sigma)
mid = 0.5 * (mu1 + mu2)
w = Sinv @ (mu1 - mu2)
slope = -w[0] / w[1]

fig, ax = plt.subplots(figsize=(7.8, 5.8))

for mu, col, lab in [(mu1, c1, r"$\mu_1$"), (mu2, c2, r"$\mu_2$")]:
    for c in (1.0, 2.0):
        ellipse(ax, mu, Sinv, c, color=col, lw=0.9, alpha=0.6)
    ax.scatter(*mu, color=col, s=100, zorder=6, edgecolor="white", linewidth=0.8)
    ax.annotate(lab, mu, xytext=(9, 9), textcoords="offset points", color=col, fontsize=13)

xs = np.linspace(-2.4, 6.4, 200)
ax.plot(xs, slope * (xs - mid[0]), color=red, lw=2.4, zorder=4)

ax.annotate("", xy=mu2, xytext=mu1,
            arrowprops=dict(arrowstyle="->", color=gray, lw=1.5, ls=(0, (4, 3))))
ax.text(3.0, -0.5, r"$\mu_1-\mu_2$", color=gray, ha="center", fontsize=11)

n = w / np.linalg.norm(w)
ax.annotate("", xy=mid + 2.0 * n, xytext=mid,
            arrowprops=dict(arrowstyle="->", color=red, lw=2.0))
ax.text(mid[0] - 1.7, mid[1] + 1.7,
        r"$\mathbf{w}=\Sigma^{-1}(\mu_1-\mu_2)$", color=red, ha="center", fontsize=11)

ax.text(2.5, 3.25, f"slope = {slope:.2f}", color=red, ha="center", fontsize=10.5)
ax.set_xlim(-2.4, 6.4)
ax.set_ylim(-3.6, 3.8)
ax.set_aspect("equal")
ax.set_xlabel(r"feature $x_1$")
ax.set_ylabel(r"feature $x_2$")
ax.set_title(r"Non-diagonal $\Sigma$: the line turns, but stays straight", fontsize=11)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig("assets/figures/lec02-linear-nondiagonal-direction.png", dpi=200)
print("w", w.round(4), "slope", round(float(slope), 4))
print("Sinv", Sinv.round(4).tolist())
