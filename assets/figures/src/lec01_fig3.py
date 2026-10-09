"""Lecture 01, Figure 3: the four-stage design loop with a feedback arrow.

Labels are English so the figure can be reused without font issues.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(7.2, 4.4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.2)
ax.axis("off")

boxes = {
    "gen": (0.6, 3.9, "1  Feature\n    generation"),
    "sel": (3.9, 3.9, "2  Feature\n    selection"),
    "des": (3.9, 1.0, "3  Classifier\n    design"),
    "eva": (7.2, 1.0, "4  System\n    evaluation"),
}
W, H = 2.6, 1.3
centers = {}
for key, (x, y, label) in boxes.items():
    box = FancyBboxPatch((x, y), W, H, boxstyle="round,pad=0.05,rounding_size=0.15",
                         linewidth=1.4, edgecolor="#0891b2", facecolor="#eef9fb")
    ax.add_patch(box)
    ax.text(x + W / 2, y + H / 2, label, ha="center", va="center", fontsize=10.5, color="#222222")
    centers[key] = (x + W / 2, y + H / 2)

def arrow(p, q, **kw):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=16, **kw))

arrow((centers["gen"][0] + W / 2, centers["gen"][1]), (centers["sel"][0] - W / 2, centers["sel"][1]),
      color="#333333", lw=1.6)
arrow((centers["sel"][0], centers["sel"][1] - H / 2), (centers["des"][0], centers["des"][1] + H / 2),
      color="#333333", lw=1.6)
arrow((centers["des"][0] + W / 2, centers["des"][1]), (centers["eva"][0] - W / 2, centers["eva"][1]),
      color="#333333", lw=1.6)

# feedback: evaluation -> feature selection (thick dashed) and -> feature generation (thin dashed)
arrow((8.5, 2.35), (6.5, 4.55), color="#0891b2", lw=2.6, linestyle="--")
ax.text(8.0, 3.6, "rework if error\nrate is poor", fontsize=8.5, color="#0891b2", ha="left", va="center")
ax.text(0.6, 5.6, "Evaluation can send the design back to any earlier stage.", fontsize=9, color="#777777", ha="left")

fig.tight_layout()
fig.savefig("assets/figures/lec01_fig3.png", dpi=200)
print("saved assets/figures/lec01_fig3.png")
