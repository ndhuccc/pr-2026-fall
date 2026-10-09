"""Figure code: lec02-bn-inference-direction.

Contrast panel for the common misconception that evidence "reverses" the
causal arrows. Left (correct): the causal structure stays left-to-right, and
only the direction of the message computation changes. Right (wrong): reading
the evidence w=1 as if causality itself ran backwards.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch

plt.rcParams["mathtext.fontset"] = "cm"
ok_c = "#2b7a3d"
no_c = "#c0392b"
gray = "#888888"
node_c = "#f2f2f2"

fig, axes = plt.subplots(1, 2, figsize=(11.6, 3.9))

# ---------------- left: correct ----------------
ax = axes[0]
xs = [0.0, 1.15, 2.30, 3.45]
r = 0.24
for i in range(3):
    ax.add_patch(FancyArrowPatch((xs[i] + r, 0.0), (xs[i + 1] - r, 0.0),
                                  arrowstyle="-|>", mutation_scale=13,
                                  color=gray, lw=1.6))
for name, x in zip(["x", "y", "z", "w"], xs):
    ax.add_patch(Circle((x, 0.0), r, facecolor=node_c, edgecolor="#333333", lw=1.3))
    ax.text(x, 0.0, rf"${name}$", ha="center", va="center", fontsize=11)

ax.add_patch(FancyArrowPatch((xs[0] + 0.05, 0.45), (xs[3] - 0.05, 0.45),
                              connectionstyle="arc3,rad=-0.22",
                              arrowstyle="-|>", mutation_scale=14,
                              color="#c0392b", lw=1.8))
ax.text(0.5 * (xs[0] + xs[3]), 0.80, r"query $P(w\mid x{=}1)$: relay forward",
        ha="center", va="bottom", fontsize=9.5, color="#c0392b")
ax.add_patch(FancyArrowPatch((xs[3] - 0.05, -0.45), (xs[0] + 0.05, -0.45),
                              connectionstyle="arc3,rad=-0.22",
                              arrowstyle="-|>", mutation_scale=14,
                              color="#2b5fa5", lw=1.8))
ax.text(0.5 * (xs[0] + xs[3]), -0.80, r"query $P(x\mid w{=}1)$: relay backward",
        ha="center", va="top", fontsize=9.5, color="#2b5fa5")

ax.text(1.72, 1.30, "causal structure stays $x\\to y\\to z\\to w$",
        ha="center", va="center", fontsize=10, color=gray, style="italic")
ax.text(-0.55, 0.0, "$\\checkmark$", ha="center", va="center",
        fontsize=20, color=ok_c, fontweight="bold")
ax.set_title("Correct: the query direction changes, not the arrows", fontsize=10.5)

# ---------------- right: misconception ----------------
ax = axes[1]
for i in range(3):
    ax.add_patch(FancyArrowPatch((xs[i + 1] - r, 0.0), (xs[i] + r, 0.0),
                                  arrowstyle="-|>", mutation_scale=13,
                                  color=gray, lw=1.6))
for name, x in zip(["x", "y", "z", "w"], xs):
    ax.add_patch(Circle((x, 0.0), r, facecolor=node_c, edgecolor="#333333", lw=1.3))
    ax.text(x, 0.0, rf"${name}$", ha="center", va="center", fontsize=11)

ax.text(1.72, 0.82, "reading evidence $w{=}1$ as\nif causality ran backwards",
        ha="center", va="center", fontsize=9.5, color=no_c)
ax.plot([0.35, 3.10], [-0.62, 0.62], color=no_c, lw=2.4)
ax.plot([0.35, 3.10], [0.62, -0.62], color=no_c, lw=2.4)
ax.text(-0.55, 0.0, "$\\times$", ha="center", va="center",
        fontsize=20, color=no_c, fontweight="bold")
ax.set_title("Misconception: evidence does not reverse causality", fontsize=10.5)

for ax in axes:
    ax.set_xlim(-0.9, 3.95)
    ax.set_ylim(-1.15, 1.55)
    ax.axis("off")

fig.tight_layout()
fig.savefig("assets/figures/lec02-bn-inference-direction.png", dpi=200)
print("saved assets/figures/lec02-bn-inference-direction.png")
