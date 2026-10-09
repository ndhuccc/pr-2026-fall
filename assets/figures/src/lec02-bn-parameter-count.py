"""Figure code: lec02-bn-parameter-count. Parameter counts for six binary features
under three independence assumptions.

Left panel: log-scale bar chart of the number of probability values to estimate.
    Naive Bayes      : sum_i 2^0           = 6
    Bayesian network : 1+1+2+4+2+4        = 14
    No assumption    : 2^6 - 1            = 63
    Ratios: 63/14 = 4.50, 63/6 = 10.50, 14-6 = 8, 63-14 = 49.
Right panel: the three dependency graphs, node layout identical (hexagon),
edge density 0 -> 6 -> 15.
All on-figure text is English / math only.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

plt.rcParams["mathtext.fontset"] = "cm"

n = 6
parents = {1: [], 2: [], 3: [2], 4: [1, 2], 5: [4], 6: [4, 5]}
naive = sum(2 ** 0 for _ in range(n))
bn = sum(2 ** len(parents[i]) for i in range(1, n + 1))
full = 2 ** n - 1
assert (naive, bn, full) == (6, 14, 63), (naive, bn, full)

nodes = [f"x{i}" for i in range(1, n + 1)]
angle = {f"x{i}": np.deg2rad(90 - 60 * (i - 1)) for i in range(1, n + 1)}
R = 1.0
pos = {k: (R * np.cos(a), R * np.sin(a)) for k, a in angle.items()}
bn_edges = [("x1", "x4"), ("x2", "x4"), ("x2", "x3"),
            ("x4", "x5"), ("x4", "x6"), ("x5", "x6")]
all_edges = [(a, b) for i, a in enumerate(nodes) for b in nodes[i + 1:]]
r = 0.17

fig = plt.figure(figsize=(13.4, 6.0))
gs = fig.add_gridspec(3, 2, width_ratios=[0.95, 1.05], hspace=0.30, wspace=0.16)


def draw_graph(ax, edges, title, border_color, arrow_lw, node_fs):
    for a, b in edges:
        # draw the arrow slightly inset so the head sits at the node rim
        arrow = FancyArrowPatch(pos[a], pos[b], arrowstyle="-|>",
                                mutation_scale=9, lw=arrow_lw,
                                color="#666666", shrinkA=r * 72 * 0.9,
                                shrinkB=r * 72 * 0.9, zorder=2)
        ax.add_patch(arrow)
    for name in nodes:
        px, py = pos[name]
        ax.add_patch(Circle((px, py), r, facecolor="#eef2f6",
                            edgecolor="#444444", lw=0.9, zorder=3))
        ax.text(px, py, f"${name[0]}_{name[1]}$", ha="center", va="center",
                fontsize=node_fs, zorder=4)
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.45, 1.35)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(plt.Rectangle((-1.32, -1.42), 2.64, 2.74, fill=False,
                               edgecolor=border_color,
                               lw=2.0 if border_color == "#dc2626" else 0.9,
                               zorder=1))
    ax.set_title(title, fontsize=11, fontweight="bold", pad=2)


# --- (a) log-scale bar chart, spanning all three rows ---
ax = fig.add_subplot(gs[:, 0])
labels = ["Naive Bayes\n(zero edges)", "Bayesian network\n(6 edges)",
          "No assumption\n(15 edges)"]
counts = [naive, bn, full]
colors = ["#8fbcd4", "#d97757", "#6a6a6a"]
xpos = np.arange(3)
bars = ax.bar(xpos, counts, width=0.55, color=colors,
              edgecolor="#333333", linewidth=0.7)
for b, v in zip(bars, counts):
    ax.text(b.get_x() + b.get_width() / 2, v * 1.12, f"{v}",
            ha="center", va="bottom", fontsize=13)
ax.set_yscale("log")
ax.set_ylim(1, 300)
ax.set_xticks(xpos, labels, fontsize=10)
ax.set_ylabel("number of probability values")
ax.set_title("(a) parameters to estimate (log scale)", fontsize=12)
ax.grid(axis="y", alpha=0.3, which="both")

ax.annotate("", xy=(1, bn * 1.85), xytext=(2, full * 0.92),
            arrowprops=dict(arrowstyle="-|>", color="#dc2626", lw=2.2))
ax.text(1.5, bn * 2.6, "4.5x fewer", ha="center", fontsize=11, color="#dc2626")
ax.annotate("", xy=(0, naive * 1.5), xytext=(1, bn * 1.02),
            arrowprops=dict(arrowstyle="-|>", color="#888888", lw=1.4))
ax.text(0.45, 7.6, "saves only 8", ha="center", fontsize=9,
        color="#666666")

# --- (b)(c)(d) three dependency graphs ---
ax1 = fig.add_subplot(gs[0, 1])
draw_graph(ax1, [], "(b) Naive Bayes: 0 edges", "#999999", 0.8, 11)
ax2 = fig.add_subplot(gs[1, 1])
draw_graph(ax2, bn_edges, "(c) Bayesian network: 6 edges (sweet spot)",
           "#dc2626", 1.1, 11)
ax3 = fig.add_subplot(gs[2, 1])
draw_graph(ax3, all_edges, "(d) No assumption: 15 edges", "#999999", 0.7, 11)

fig.savefig("assets/figures/lec02-bn-parameter-count.png", dpi=200,
            bbox_inches="tight", facecolor="white")
print("saved assets/figures/lec02-bn-parameter-count.png")
print("naive", naive, "bn", bn, "full", full)
print("ratios", round(full / bn, 4), round(full / naive, 4),
      "edges", len(all_edges), len(bn_edges))
