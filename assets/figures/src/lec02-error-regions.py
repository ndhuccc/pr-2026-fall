"""Figure code: lec02-error-regions. Error probability for two equal-prior Gaussians.

p(x|w1) = N(-1, 1) and p(x|w2) = N(+1, 1), P(w1) = P(w2) = 0.5.
Panel (a): densities with the error tails shaded for threshold x0 = 0.
Panel (b): total error Pe(x0) versus threshold; the minimum is at x0 = 0 (the intersection).
"""
import numpy as np
import matplotlib.pyplot as plt
from math import erf, sqrt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"


def Phi(z):
    return 0.5 * (1 + np.vectorize(erf)(np.asarray(z) / sqrt(2)))


def gauss(x, m):
    return np.exp(-(x - m) ** 2 / 2) / np.sqrt(2 * np.pi)


def Pe(x0, mu1=-1.0, mu2=1.0, s=1.0, P=0.5):
    # error = P(w2) * P(x in R1 | w2) + P(w1) * P(x in R2 | w1)
    return P * Phi((x0 - mu2) / s) + P * (1 - Phi((x0 - mu1) / s))


x = np.linspace(-4, 4, 800)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.0))

# panel (a)
ax1.plot(x, gauss(x, -1), color=c1, lw=2.0, label=r"$p(x\mid\omega_1)$")
ax1.plot(x, gauss(x, 1), color=c2, lw=2.0, label=r"$p(x\mid\omega_2)$")
left = x <= 0
right = x >= 0
ax1.fill_between(x[left], 0, gauss(x[left], 1) * 0.5, color=c2, alpha=0.35,
                 label="error: $\\omega_2$ judged $\\omega_1$")
ax1.fill_between(x[right], 0, gauss(x[right], -1) * 0.5, color=c1, alpha=0.35,
                 label="error: $\\omega_1$ judged $\\omega_2$")
ax1.axvline(0, color="#333333", lw=1.2)
ax1.set_xlabel("feature $x$")
ax1.set_ylabel("density")
ax1.set_title(f"(a) threshold $x_0=0$: $P_e$ = {Pe(0.0):.4f}", fontsize=10)
ax1.legend(frameon=False, fontsize=8, loc="upper left")
ax1.grid(alpha=0.3)

# panel (b)
t = np.linspace(-1.5, 1.5, 301)
ax2.plot(t, Pe(t), color="#333333", lw=1.8)
offsets = {-0.5: (-88, 14), 0.0: (-125, -2), 0.5: (14, -34)}
for x0, off in offsets.items():
    ax2.scatter([x0], [Pe(x0)], color="#d97757" if x0 == 0 else "#999999", zorder=3, s=36)
    ax2.annotate(f"$x_0={x0:+.1f}$\n$P_e$={Pe(x0):.4f}" if x0 else "$x_0=0$\n$P_e$=" + f"{Pe(0.0):.4f}",
                 (x0, Pe(x0)), textcoords="offset points", xytext=off, fontsize=8)
ax2.set_xlabel("threshold $x_0$")
ax2.set_ylabel(r"$P_e(x_0)$")
ax2.set_title("(b) the Bayes threshold gives the smallest $P_e$", fontsize=10)
ax2.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-error-regions.png", dpi=200)
print("saved assets/figures/lec02-error-regions.png")
print("Pe at -0.5, 0, 0.5:", [round(float(Pe(v)), 4) for v in (-0.5, 0.0, 0.5)])
