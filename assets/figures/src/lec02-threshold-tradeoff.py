"""Figure code: lec02-threshold-tradeoff. Moving the threshold trades one error for the other.

Same setting as lec02-error-regions: p(x|w1)=N(-1,1), p(x|w2)=N(+1,1), P(w1)=P(w2)=0.5.
The two error terms and their sum P_e(x0) are plotted against the threshold x0.
"""
import numpy as np
import matplotlib.pyplot as plt
from math import erf, sqrt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"
P = 0.5


def Phi(z):
    return 0.5 * (1 + np.vectorize(erf)(np.asarray(z) / sqrt(2)))


def err_w2_as_w1(x0):   # P(w2) P(x <= x0 | w2)
    return P * Phi(x0 - 1.0)


def err_w1_as_w2(x0):   # P(w1) P(x >= x0 | w1)
    return P * (1 - Phi(x0 + 1.0))


t = np.linspace(-1.5, 1.5, 301)
fig, ax = plt.subplots(figsize=(8.4, 5.0))
ax.plot(t, err_w2_as_w1(t), color=c2, lw=2.0, label=r"$\omega_2$ judged $\omega_1$")
ax.plot(t, err_w1_as_w2(t), color=c1, lw=2.0, label=r"$\omega_1$ judged $\omega_2$")
ax.plot(t, err_w2_as_w1(t) + err_w1_as_w2(t), color="#333333", lw=2.2, label=r"total $P_e(x_0)$")
ax.axvline(0, color="#e0995f", ls="--", lw=1.2)
for x0 in (-0.5, 0.0, 0.5):
    pe = float(err_w2_as_w1(x0) + err_w1_as_w2(x0))
    ax.scatter([x0], [pe], color="#333333", s=28, zorder=3)
    if x0 > 0:
        xy, ha = (8, -48), "left"
    elif x0 < 0:
        xy, ha = (-8, -48), "right"
    else:
        xy, ha = (0, 58), "center"          # above the curves, where nothing else is drawn
    ax.annotate(f"$x_0={x0:+.1f}$\n$P_e={pe:.4f}$", (x0, pe), textcoords="offset points",
                xytext=xy, ha=ha, fontsize=9)
ax.set_xlabel("threshold $x_0$")
ax.set_ylabel("error contribution")
ax.set_title("Moving the threshold: one error falls, the other rises", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="upper center")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-threshold-tradeoff.png", dpi=200)
print("saved assets/figures/lec02-threshold-tradeoff.png")
for x0 in (-0.5, 0.0, 0.5):
    print("x0", x0, "e2", round(float(err_w2_as_w1(x0)), 4), "e1", round(float(err_w1_as_w2(x0)), 4),
          "Pe", round(float(err_w2_as_w1(x0) + err_w1_as_w2(x0)), 4))
