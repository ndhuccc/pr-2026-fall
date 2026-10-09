"""Figure code: lec02-monotone-transform. A strictly increasing f preserves the order of the scores.

f(p)=sqrt(p) applied to the posteriors 0.4286 and 0.5714 from lecture Section 1 gives 0.6547 and 0.7559.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
c1, c2 = "#6a9fd6", "#d97757"

p = np.linspace(0, 1, 400)
p1, p2 = 0.4286, 0.5714
g1, g2 = np.sqrt(p1), np.sqrt(p2)

fig, ax = plt.subplots(figsize=(8.4, 5.0))
ax.plot(p, np.sqrt(p), color="#333333", lw=2.0, label=r"$f(p)=\sqrt{p}$")
ax.scatter([p1, p2], [g1, g2], color=[c1, c2], s=52, zorder=3)
ax.plot([p1, p1], [0, g1], color=c1, ls="--", lw=1.0)
ax.plot([p2, p2], [0, g2], color=c2, ls="--", lw=1.0)
ax.annotate(rf"$\omega_1$: {p1:.4f} $\to$ {g1:.4f}", (p1, g1), textcoords="offset points",
            xytext=(-6, 52), ha="right", fontsize=9)
ax.annotate(rf"$\omega_2$: {p2:.4f} $\to$ {g2:.4f}", (p2, g2), textcoords="offset points",
            xytext=(8, -90), ha="left", fontsize=9)
ax.set_xlabel("posterior $P(\\omega_i\\mid x)$")
ax.set_ylabel("score $g_i$")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.set_title("Monotone transform: the larger score stays larger", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="lower right")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig("assets/figures/lec02-monotone-transform.png", dpi=200)
print("saved assets/figures/lec02-monotone-transform.png")
print("scores", round(g1, 4), round(g2, 4), "order preserved", g2 > g1)
