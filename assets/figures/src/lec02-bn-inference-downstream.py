"""Figure code: lec02-bn-inference-downstream.

Scenario (a): evidence at x = 1, messages flow downstream. Three stations
(y, z, w) each read the single number handed over by the previous station,
multiply it by their own CPT, and hand on one number. All values are computed
here and match exact enumeration: P(y=1|x=1)=0.40, P(z=1|x=1)=0.46,
P(w=0|x=1)=0.631.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["mathtext.fontset"] = "cm"
red = "#c0392b"

P_y1_x1 = 0.4
P_y0_x1 = 1 - P_y1_x1
P_z1_y1, P_z1_y0 = 0.25, 0.6
P_z1_x1 = P_z1_y1 * P_y1_x1 + P_z1_y0 * P_y0_x1
P_z0_x1 = 1 - P_z1_x1
P_w1_z1, P_w1_z0 = 0.45, 0.3
P_w0_x1 = (1 - P_w1_z1) * P_z1_x1 + (1 - P_w1_z0) * P_z0_x1

rows = [
    ("station $y$", r"$x{=}1$ already observed",
     r"$P(y{=}1\mid x{=}1)=0.40$"),
    ("station $z$", r"carry in $P(y{=}1\mid x{=}1)=0.40$",
     r"$0.25(0.40)+0.60(0.60)=0.46$"),
    ("station $w$", r"carry in $P(z{=}1\mid x{=}1)=0.46$",
     r"$0.55(0.46)+0.70(0.54)=0.631$"),
]

fig, ax = plt.subplots(figsize=(10.6, 3.6))
ax.set_xlim(0, 10.6)
ax.set_ylim(0, 3.6)
ax.axis("off")

ax.text(5.3, 3.32, "Scenario (a): evidence at $x{=}1$, messages flow downstream",
        ha="center", va="center", fontsize=12)

y_head = 2.88
for xc, lab in [(1.5, "station"), (4.3, "reads from the previous station"),
                (8.2, "hands on")]:
    ax.text(xc, y_head, lab, ha="center", va="center", fontsize=9.6,
            color="#555555")

y_centers = [2.20, 1.42, 0.64]
for (name, inc, out), yc in zip(rows, y_centers):
    box = FancyBboxPatch((0.25, yc - 0.27), 2.5, 0.54,
                          boxstyle="round,pad=0.04", facecolor="#f7f7f7",
                          edgecolor="#777777", lw=1.1)
    ax.add_patch(box)
    ax.text(1.5, yc, name, ha="center", va="center", fontsize=10)
    ax.text(4.3, yc, inc, ha="center", va="center", fontsize=9.4)
    ax.text(8.2, yc, out, ha="center", va="center", fontsize=10,
            color=red, fontweight="bold")
    if yc > 1.0:
        ax.add_patch(FancyArrowPatch((9.45, yc), (9.45, yc - 0.42),
                                      connectionstyle="arc3,rad=-0.55",
                                      arrowstyle="-|>", mutation_scale=14,
                                      color=red, lw=1.4))

ax.text(5.3, 0.10, "each station uses only the incoming number and its own CPT: "
        "one pass, no re-summing over the whole chain",
        ha="center", va="center", fontsize=9.2, style="italic", color="#555555")

fig.tight_layout()
fig.savefig("assets/figures/lec02-bn-inference-downstream.png", dpi=200)
print("saved assets/figures/lec02-bn-inference-downstream.png")
print("P(y=1|x=1)", round(P_y1_x1, 4), "P(z=1|x=1)", round(P_z1_x1, 4),
      "P(z=0|x=1)", round(P_z0_x1, 4), "P(w=0|x=1)", round(P_w0_x1, 4))
