"""Figure code: lec02-knn-vote-panel.

The 11-nearest-neighbour vote (Figure 2.25 analogue). Around the query point
(the star) the 11 nearest training samples are 7 red and 4 black, so the vote
is red: 7/11 = 0.636... against 4/11 = 0.363....

The positions are computed here; only the counts (7 red, 4 black, k=11) are
the numbers quoted in the text.
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["mathtext.fontset"] = "cm"
C_RED, C_BLACK, C_OUT = "#dc2626", "#222222", "#b9b9b9"

rng = np.random.default_rng(11)

# 7 red at radius 1.00, 4 black at radius 1.05 -> the closest 11 are 7+4.
ang_r = np.linspace(0.15, 2 * np.pi - 0.15, 7) + 0.10
red = np.c_[1.00 * np.cos(ang_r), 1.00 * np.sin(ang_r)]
ang_b = np.array([0.9, 2.2, 3.6, 5.1])
black = np.c_[1.05 * np.cos(ang_b), 1.05 * np.sin(ang_b)]
# 12 further points that are NOT among the 11 nearest neighbours
far_ang = rng.uniform(0, 2 * np.pi, 12)
far_r = rng.uniform(2.3, 2.9, 12)
far = np.c_[far_r * np.cos(far_ang), far_r * np.sin(far_ang)]

fig, ax = plt.subplots(figsize=(6.6, 6.2))
ax.scatter(red[:, 0], red[:, 1], s=85, c=C_RED, edgecolors="white",
           linewidths=1.0, zorder=4, label="red class (7 in the vote)")
ax.scatter(black[:, 0], black[:, 1], s=85, c=C_BLACK, edgecolors="white",
           linewidths=1.0, zorder=4, label="black class (4 in the vote)")
for i in range(12):
    ax.scatter(far[i, 0], far[i, 1], s=45, c=C_OUT, alpha=0.55, zorder=2)
ax.scatter([], [], s=45, c=C_OUT, alpha=0.6, label="outside the 11 (not counted)")

circ = plt.Circle((0, 0), 1.05, fill=False, ls="--", lw=1.4, color="#333333",
                   zorder=3)
ax.add_patch(circ)
ax.plot([0], [0], marker="*", ms=20, mfc="white", mec="#111111", mew=1.6,
        zorder=6)
ax.annotate("query point $\\mathbf{x}$", (0, 0), textcoords="offset points",
            xytext=(-96, -22), fontsize=9,
            arrowprops=dict(arrowstyle="->", lw=0.9))
ax.text(0.0, 2.08, "vote: 7 red vs 4 black  $\\rightarrow$  red\n"
                   "$\\hat{c}=\\arg\\max_i k_i$,   $k_1{=}7,\\ k_2{=}4,\\ k{=}11$",
        ha="center", fontsize=9.5)
ax.text(1.12, 0.28, "$r_{11}$: 11th neighbour", fontsize=8.5, color="#333333")

ax.set_aspect("equal")
ax.set_xlim(-3.1, 3.1)
ax.set_ylim(-3.1, 2.9)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("11-nearest-neighbour rule: 7 red, 4 black", fontsize=10)
ax.legend(frameon=False, fontsize=8.5, loc="lower left")
ax.grid(alpha=0.25)

fig.tight_layout()
fig.savefig("assets/figures/lec02-knn-vote-panel.png", dpi=200)
print("saved lec02-knn-vote-panel.png")
print("red in vote", len(red), "black in vote", len(black), "k", len(red) + len(black))
print("share red", round(7 / 11, 4), "share black", round(4 / 11, 4))
