"""Lecture 01, Figure 1: two discriminant functions on a 1-D feature x in [0, 1].

g1(x) = x and g2(x) = 1 - x. Decide class 1 where g1 > g2, i.e. x > 0.5.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"

x = np.linspace(0.0, 1.0, 400)
g1 = x
g2 = 1.0 - x

fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.plot(x, g1, color="#d97757", lw=2.2, label=r"$g_1(x)=x$")
ax.plot(x, g2, color="#6a9fd6", lw=2.2, label=r"$g_2(x)=1-x$")
ax.axvline(0.5, color="#e0995f", ls="--", lw=1.6, label=r"boundary $x=0.5$")

for xv in (0.3, 0.8):
    ax.plot([xv, xv], [0, 1], color="#888888", lw=0.8, alpha=0.6)
ax.scatter([0.3, 0.8], [0.3, 0.8], color="#d97757", zorder=3)
ax.scatter([0.3, 0.8], [0.7, 0.2], color="#6a9fd6", zorder=3)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"feature $x$")
ax.set_ylabel("score")
ax.grid(alpha=0.3)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), frameon=False, ncol=3, fontsize=9)
fig.tight_layout()
fig.savefig("assets/figures/lec01_fig1.png", dpi=200)
print("saved assets/figures/lec01_fig1.png")
