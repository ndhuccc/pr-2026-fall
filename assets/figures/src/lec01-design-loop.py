"""Figure code: lec01-design-loop. The four-stage design loop with TWO feedback paths.

Feedback paths (both start at stage 4, System evaluation):
  - thick dashed teal arrow: back to stage 2, Feature selection
  - thin dashed grey route: back to stage 1, Feature generation (routed above the boxes)
Labels are English so the figure can be reused without font issues.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(7.6, 4.6))
ax.set_xlim(0, 11.2)
ax.set_ylim(0, 6.6)
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


# forward path (solid)
arrow((centers["gen"][0] + W / 2, centers["gen"][1]), (centers["sel"][0] - W / 2, centers["sel"][1]),
      color="#333333", lw=1.6)
arrow((centers["sel"][0], centers["sel"][1] - H / 2), (centers["des"][0], centers["des"][1] + H / 2),
      color="#333333", lw=1.6)
arrow((centers["des"][0] + W / 2, centers["des"][1]), (centers["eva"][0] - W / 2, centers["eva"][1]),
      color="#333333", lw=1.6)

# feedback 1 (thick dashed): evaluation -> feature selection
arrow((8.0, 2.3), (6.5, 4.3), color="#0891b2", lw=2.6, linestyle="--")
ax.text(5.45, 3.0, "rework:\nselect again", fontsize=8.5, color="#0891b2", ha="left", va="center")

# feedback 2 (thin dashed): evaluation -> feature generation, routed above the boxes
route_x_right, route_y_top, route_x_left = 9.6, 6.1, centers["gen"][0]
ax.plot([9.6, 9.6], [2.3, route_y_top], color="#777777", lw=1.2, linestyle="--")
ax.plot([9.6, route_x_left], [route_y_top, route_y_top], color="#777777", lw=1.2, linestyle="--")
arrow((route_x_left, route_y_top), (route_x_left, centers["gen"][1] + H / 2 + 0.05),
      color="#777777", lw=1.2, linestyle="--")
ax.text(4.2, route_y_top + 0.18, "rework: generate new features", fontsize=8.5, color="#555555",
        ha="left", va="bottom")

ax.text(0.6, 0.35, "Two feedback paths: back to stage 2 (thick) or back to stage 1 (thin).",
        fontsize=9, color="#555555", ha="left")

fig.tight_layout()
fig.savefig("assets/figures/lec01-design-loop.png", dpi=200)
print("saved assets/figures/lec01-design-loop.png")
