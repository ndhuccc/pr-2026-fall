"""Figure code: lec02-bn-structure. A six-node Bayesian network as a DAG.

Feature nodes x1..x6 (all binary). Directed edges (arrows point to the child):
    x1 -> x4, x2 -> x4, x2 -> x3, x4 -> x5, x4 -> x6, x5 -> x6
Parent sets: A1 = A2 = {} , A3 = {x2}, A4 = {x1, x2}, A5 = {x4}, A6 = {x4, x5}.
Number of probability values to estimate: 1 + 1 + 2 + 4 + 2 + 4 = 14.
All on-figure text is English / math only.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

plt.rcParams["mathtext.fontset"] = "cm"

pos = {
    "x1": (0.0, 3.2),
    "x2": (0.0, 2.0),
    "x3": (1.9, 2.0),
    "x4": (1.9, 3.2),
    "x5": (3.7, 3.2),
    "x6": (2.9, 1.0),
}
edges = [
    ("x1", "x4"), ("x2", "x4"), ("x2", "x3"),
    ("x4", "x5"), ("x4", "x6"), ("x5", "x6"),
]
radius = 0.28

fig, ax = plt.subplots(figsize=(7.2, 5.0))
ax.set_aspect("equal")

for a, b in edges:
    p, q = pos[a], pos[b]
    arrow = FancyArrowPatch(
        p, q, arrowstyle="-|>", mutation_scale=16,
        lw=1.6, color="#333333", shrinkA=20, shrinkB=22, zorder=2,
    )
    ax.add_patch(arrow)

roots = {"x1", "x2"}
for name, (px, py) in pos.items():
    face = "#f2d6c4" if name in roots else "#cfe0f2"
    ax.add_patch(Circle((px, py), radius, facecolor=face,
                        edgecolor="#333333", lw=1.4, zorder=3))
    ax.text(px, py, f"${name[0]}_{name[1]}$", ha="center", va="center",
            fontsize=14, zorder=4)

ax.text(0.0, 3.2 + radius + 0.28, "root", ha="center", va="bottom",
        fontsize=9, color="#a0522d")
ax.text(0.0, 2.0 - radius - 0.34, "root", ha="center", va="top",
        fontsize=9, color="#a0522d")
ax.text(2.9, 1.0 - radius - 0.22,
        "6 directed edges in total", ha="center", va="top",
        fontsize=10, color="#333333")

ax.set_xlim(-0.9, 4.6)
ax.set_ylim(-0.2, 4.35)
ax.axis("off")
fig.tight_layout()
fig.savefig("assets/figures/lec02-bn-structure.png", dpi=200,
            bbox_inches="tight", facecolor="white")
print("saved assets/figures/lec02-bn-structure.png")
