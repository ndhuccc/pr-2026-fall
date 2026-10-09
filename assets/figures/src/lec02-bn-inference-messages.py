"""Figure code: lec02-bn-inference-messages.

Chain Bayesian network x -> y -> z -> w (all binary) with two message flows:
red downstream arrows on top (evidence x=1), blue upstream arrows below
(evidence w=1). Each arrow carries the posterior of the arrow's target given
the evidence, and each node carries a small CPT box.

Numbers from the textbook example (Section 2.7): P(y=1|x=1)=0.40,
P(z=1|x=1)=0.46, P(w=0|x=1)=0.631, P(z=1|w=1)=0.575, P(x=0|w=1)=0.403.
The upstream intermediate P(y=1|w=1)=0.327 is computed by the same exact
enumeration scheme.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch, Arc

plt.rcParams["mathtext.fontset"] = "cm"
down_c = "#c0392b"
up_c = "#2b5fa5"
node_c = "#f2f2f2"

nodes = ["x", "y", "z", "w"]
xs = [0.0, 1.7, 3.4, 5.1]
y0 = 0.0
r = 0.34

fig, ax = plt.subplots(figsize=(11.0, 6.2))

# structural edges (gray)
for i in range(3):
    ax.add_patch(FancyArrowPatch((xs[i] + r, y0), (xs[i + 1] - r, y0),
                                  arrowstyle="-|>", mutation_scale=16,
                                  color="#777777", lw=1.6, zorder=2))

# nodes
for name, x in zip(nodes, xs):
    ax.add_patch(Circle((x, y0), r, facecolor=node_c, edgecolor="#333333",
                        lw=1.4, zorder=3))
    ax.text(x, y0, rf"${name}$", ha="center", va="center", fontsize=15, zorder=4)

# downstream arrows (red), above the chain
down_lab = [r"$P(y{=}1\mid x{=}1)=0.40$",
            r"$P(z{=}1\mid x{=}1)=0.46$",
            r"$P(w{=}0\mid x{=}1)=0.631$"]
yd = 0.85
for i in range(3):
    ax.add_patch(FancyArrowPatch((xs[i] + r + 0.02, yd), (xs[i + 1] - r - 0.02, yd),
                                  arrowstyle="-|>", mutation_scale=18,
                                  color=down_c, lw=2.0, zorder=2))
    ax.text(0.5 * (xs[i] + xs[i + 1]), yd + 0.16, down_lab[i],
            ha="center", va="bottom", fontsize=9, color=down_c)

# upstream arrows (blue), below the chain
up_lab = [r"$P(z{=}1\mid w{=}1)=0.575$",
          r"$P(y{=}1\mid w{=}1)=0.327$",
          r"$P(x{=}0\mid w{=}1)=0.403$"]
yu = -0.85
for i in range(3):
    ax.add_patch(FancyArrowPatch((xs[i + 1] - r - 0.02, yu), (xs[i] + r + 0.02, yu),
                                  arrowstyle="-|>", mutation_scale=18,
                                  color=up_c, lw=2.0, zorder=2))
for i in range(3):
    txt = up_lab[i]
    ax.text(0.5 * (xs[i] + xs[i + 1]), yu - 0.16, txt,
            ha="center", va="top", fontsize=9, color=up_c)

# evidence badges
ax.text(xs[0], y0 + 0.62, r"evidence $x{=}1$", ha="center", va="bottom",
        fontsize=9.5, color=down_c,
        bbox=dict(boxstyle="round,pad=0.28", fc="#fdecea", ec=down_c, lw=1.0))
ax.text(xs[3], y0 + 0.62, r"evidence $w{=}1$", ha="center", va="bottom",
        fontsize=9.5, color=up_c,
        bbox=dict(boxstyle="round,pad=0.28", fc="#eaf0fb", ec=up_c, lw=1.0))

# CPT boxes hanging under each node
cpts = [["$P(x{=}1)=0.6$", "$P(x{=}0)=0.4$"],
        ["$P(y{=}1\\mid x{=}1)=0.4$", "$P(y{=}1\\mid x{=}0)=0.3$"],
        ["$P(z{=}1\\mid y{=}1)=0.25$", "$P(z{=}1\\mid y{=}0)=0.6$"],
        ["$P(w{=}1\\mid z{=}1)=0.45$", "$P(w{=}1\\mid z{=}0)=0.3$"]]
for x, lines in zip(xs, cpts):
    box = FancyBboxPatch((x - 0.78, -2.55), 1.56, 1.0,
                          boxstyle="round,pad=0.06", facecolor="#fbfbfb",
                          edgecolor="#999999", lw=1.0, zorder=1)
    ax.add_patch(box)
    ax.text(x, -1.68, "CPT", ha="center", va="bottom", fontsize=8.2,
            color="#666666", zorder=2)
    ax.text(x, -2.05, lines[0], ha="center", va="center", fontsize=8.0, zorder=2)
    ax.text(x, -2.32, lines[1], ha="center", va="center", fontsize=8.0, zorder=2)

# brute-force bar spanning the whole chain, crossed out
ybar = 1.35
ax.add_patch(FancyArrowPatch((xs[0], ybar), (xs[3], ybar),
                             arrowstyle="<|-|>", mutation_scale=12,
                             ls=(0, (5, 4)), color="#aaaaaa", lw=1.3, zorder=1))
mx = 0.5 * (xs[0] + xs[3])
ax.plot([mx - 0.13, mx + 0.13], [ybar - 0.13, ybar + 0.13],
        color=down_c, lw=2.0, zorder=5)
ax.plot([mx - 0.13, mx + 0.13], [ybar + 0.13, ybar - 0.13],
        color=down_c, lw=2.0, zorder=5)
ax.text(mx, ybar + 0.14, r"brute force: sum over all $y,z$ (cost $L^5$)",
        ha="center", va="bottom", fontsize=9.5, color="#777777")

# flow labels
ax.text(-0.85, yd, "downstream\n(predict)", ha="center", va="center",
        fontsize=9.5, color=down_c, style="italic")
ax.text(-0.85, yu, "upstream\n(attribute)", ha="center", va="center",
        fontsize=9.5, color=up_c, style="italic")

ax.set_xlim(-1.6, 6.0)
ax.set_ylim(-2.85, 1.95)
ax.axis("off")
ax.set_title("One chain, two message directions: relay the number, do not recompute",
             fontsize=11.5)
fig.tight_layout()
fig.savefig("assets/figures/lec02-bn-inference-messages.png", dpi=200)
print("saved assets/figures/lec02-bn-inference-messages.png")
