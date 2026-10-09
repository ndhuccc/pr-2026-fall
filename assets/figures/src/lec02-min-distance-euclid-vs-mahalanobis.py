"""Figure code: lec02-min-distance-euclid-vs-mahalanobis.

Shared covariance Sigma = [[1.1, 0.3], [0.3, 1.9]],
means mu1 = [0, 0], mu2 = [3, 3], test point x = [1.0, 2.2].
Euclidean: d^2(x, mu1) = 5.84, d^2(x, mu2) = 4.64 -> picks mu2.
Mahalanobis: d^2(x, mu1) = 2.952, d^2(x, mu2) = 3.672 -> picks mu1.
Left: circles through x; right: ellipses through x.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2, red = "#6a9fd6", "#d97757", "#dc2626"


def ellipse(ax, mu, Sinv, c, **kw):
    vals, vecs = np.linalg.eigh(Sinv)
    t = np.linspace(0.0, 2.0 * np.pi, 400)
    pts = vecs @ np.diag(c / np.sqrt(vals)) @ np.vstack([np.cos(t), np.sin(t)])
    ax.plot(mu[0] + pts[0], mu[1] + pts[1], **kw)


mu1 = np.array([0.0, 0.0])
mu2 = np.array([3.0, 3.0])
x = np.array([1.0, 2.2])
Sigma = np.array([[1.1, 0.3], [0.3, 1.9]])
Sinv = np.linalg.inv(Sigma)

dE1 = np.linalg.norm(x - mu1)
dE2 = np.linalg.norm(x - mu2)
q1 = x - mu1
q2 = x - mu2
dM1 = np.sqrt(q1 @ Sinv @ q1)
dM2 = np.sqrt(q2 @ Sinv @ q2)

fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.4))

ax = axes[0]
t = np.linspace(0.0, 2.0 * np.pi, 400)
for mu, r, col, lab in [(mu1, dE1, c1, r"$\mu_1$"), (mu2, dE2, c2, r"$\mu_2$")]:
    ax.plot(mu[0] + r * np.cos(t), mu[1] + r * np.sin(t), color=col, lw=1.8)
    ax.scatter(*mu, color=col, s=90, zorder=6, edgecolor="white", linewidth=0.8)
    ax.annotate(lab, mu, xytext=(8, 8), textcoords="offset points", color=col, fontsize=13)
ax.scatter(*x, marker="*", s=340, color=red, zorder=7)
ax.annotate(r"$\mathbf{x}$", x, xytext=(12, -20), textcoords="offset points", color=red, fontsize=13)
ax.text(-0.4, 2.9, f"$d_E^2(\\mu_1,\\mathbf{{x}})={dE1**2:.2f}$", color=c1, fontsize=10)
ax.text(3.0, -1.15, f"$d_E^2(\\mu_2,\\mathbf{{x}})={dE2**2:.2f}$", color=c2, ha="center", fontsize=10)
ax.set_title("(a) Euclidean: equal-distance curves are circles", fontsize=11)

ax = axes[1]
for mu, r, col, lab in [(mu1, dM1, c1, r"$\mu_1$"), (mu2, dM2, c2, r"$\mu_2$")]:
    ellipse(ax, mu, Sinv, r, color=col, lw=1.8)
    ax.scatter(*mu, color=col, s=90, zorder=6, edgecolor="white", linewidth=0.8)
    ax.annotate(lab, mu, xytext=(8, 8), textcoords="offset points", color=col, fontsize=13)
ax.scatter(*x, marker="*", s=340, color=red, zorder=7)
ax.annotate(r"$\mathbf{x}$", x, xytext=(12, -20), textcoords="offset points", color=red, fontsize=13)
ax.text(-1.8, 3.4, f"$d_M^2(\\mu_1,\\mathbf{{x}})={dM1**2:.3f}$", color=c1, fontsize=10)
ax.text(3.0, -1.55, f"$d_M^2(\\mu_2,\\mathbf{{x}})={dM2**2:.3f}$", color=c2, ha="center", fontsize=10)
ax.set_title("(b) Mahalanobis: equal-distance curves are ellipses", fontsize=11)

for ax in axes:
    ax.set_xlim(-2.6, 5.4)
    ax.set_ylim(-2.2, 5.6)
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)
    ax.set_xlabel(r"feature $x_1$")
axes[0].set_ylabel(r"feature $x_2$")

fig.suptitle("Same point, two distance rules: Euclidean picks $\\mu_2$, Mahalanobis picks $\\mu_1$",
             fontsize=11.5)
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig("assets/figures/lec02-min-distance-euclid-vs-mahalanobis.png", dpi=200)
print("dE^2", round(dE1 ** 2, 4), round(dE2 ** 2, 4))
print("dM^2", round(dM1 ** 2, 4), round(dM2 ** 2, 4))
print("Sigma det", round(float(np.linalg.det(Sigma)), 4), "Sinv", Sinv.round(4).tolist())
