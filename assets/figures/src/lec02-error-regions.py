"""Figure code: lec02-error-regions. Error probability for two equal-prior Gaussians.

p(x|w1) = N(-1, 1) and p(x|w2) = N(+1, 1), P(w1) = P(w2) = 0.5.
Panel (a): the weighted densities P(w_i) p(x|w_i) for threshold x0 = 0. The shaded areas lie
exactly under the plotted curves, on the wrong side of the threshold; each has area 0.0793.
Panel (b): total error Pe(x0) versus threshold; the minimum is at x0 = 0 (the intersection).
"""
import numpy as np
import matplotlib.pyplot as plt
from math import erf, sqrt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"
P = 0.5


def Phi(z):
    return 0.5 * (1 + np.vectorize(erf)(np.asarray(z) / sqrt(2)))


def gauss(x, m):
    return np.exp(-(x - m) ** 2 / 2) / np.sqrt(2 * np.pi)


def Pe(x0, mu1=-1.0, mu2=1.0, s=1.0, P=P):
    # error = P(w2) * P(x in R1 | w2) + P(w1) * P(x in R2 | w1)
    return P * Phi((x0 - mu2) / s) + P * (1 - Phi((x0 - mu1) / s))


x = np.linspace(-4, 4, 800)
w1 = P * gauss(x, -1)   # P(w1) p(x|w1)
w2 = P * gauss(x, 1)    # P(w2) p(x|w2)
left = x <= 0
right = x >= 0
area_left = P * Phi(0 - 1)        # integral of P(w2) p(x|w2) for x <= 0
area_right = P * (1 - Phi(0 + 1))  # integral of P(w1) p(x|w1) for x >= 0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.8))

# panel (a): weighted densities; shading lies exactly under the plotted curves
ax1.plot(x, w1, color=c1, lw=2.0, label=r"$P(\omega_1)\,p(x\mid\omega_1)$")
ax1.plot(x, w2, color=c2, lw=2.0, label=r"$P(\omega_2)\,p(x\mid\omega_2)$")
ax1.fill_between(x[left], 0, w2[left], color=c2, alpha=0.35,
                 label=f"error: $\\omega_2$ judged $\\omega_1$ (area {area_left:.4f})")
ax1.fill_between(x[right], 0, w1[right], color=c1, alpha=0.35,
                 label=f"error: $\\omega_1$ judged $\\omega_2$ (area {area_right:.4f})")
ax1.axvline(0, color="#333333", lw=1.2)
ax1.set_xlabel("feature $x$")
ax1.set_ylabel(r"$P(\omega_i)\,p(x\mid\omega_i)$")
ax1.set_title(f"(a) threshold $x_0=0$: $P_e$ = {Pe(0.0):.4f}", fontsize=10)
ax1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=False, fontsize=8)
ax1.grid(alpha=0.3)

# panel (b)
t = np.linspace(-1.5, 1.5, 301)
ax2.plot(t, Pe(t), color="#333333", lw=1.8)
offsets = {-0.5: (-88, 14), 0.0: (-125, -2), 0.5: (14, -34)}
for x0, off in offsets.items():
    ax2.scatter([x0], [Pe(x0)], color="#d97757" if x0 == 0 else "#999999", zorder=3, s=36)
    label = f"$x_0={x0:+.1f}$" if x0 else "$x_0=0$"
    ax2.annotate(f"{label}\n$P_e$={Pe(x0):.4f}", (x0, Pe(x0)), textcoords="offset points",
                 xytext=off, fontsize=8)
ax2.set_xlabel("threshold $x_0$")
ax2.set_ylabel(r"$P_e(x_0)$")
ax2.set_title("(b) the Bayes threshold gives the smallest $P_e$", fontsize=10)
ax2.grid(alpha=0.3)

fig.tight_layout()
fig.savefig("assets/figures/lec02-error-regions.png", dpi=200)
print("saved assets/figures/lec02-error-regions.png")
print("areas:", round(area_left, 4), round(area_right, 4), "total", round(area_left + area_right, 4))
