"""Figure code: lec02-bn-conditional-independence. Marginal dependence versus
conditional independence along the chain x1 -> x2 -> x3.

Numbers (computed by exact enumeration, all consistent with the lecture):
  p(x1=1)=0.5, p(x2=1|x1=1)=0.9, p(x2=1|x1=0)=0.1,
  p(x3=1|x2=1)=0.8, p(x3=1|x2=0)=0.2.
  Without observing x2:  p(x3=1|x1=1)=0.74, p(x3=1|x1=0)=0.26  -> dependent.
  Given x2:              p(x3=1|x2=1,x1=1)=p(x3=1|x2=1,x1=0)=0.80,
                         p(x3=1|x2=0,x1=1)=p(x3=1|x2=0,x1=0)=0.20 -> independent.
All on-figure text is English / math only.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

plt.rcParams["mathtext.fontset"] = "cm"

p1 = 0.5
p21, p20 = 0.9, 0.1
p31, p30 = 0.8, 0.2
p2 = p1 * p21 + (1 - p1) * p20
x3_given_x1_1 = p21 * p31 + (1 - p21) * p30
x3_given_x1_0 = p20 * p31 + (1 - p20) * p30
assert abs(x3_given_x1_1 - 0.74) < 1e-12 and abs(x3_given_x1_0 - 0.26) < 1e-12

fig = plt.figure(figsize=(12.4, 4.4))
gs = fig.add_gridspec(1, 3, width_ratios=[0.85, 1.0, 1.15], wspace=0.42)

# --- (a) the chain ---
axc = fig.add_subplot(gs[0, 0])
axc.set_aspect("equal")
axc.axis("off")
xs = [0.0, 1.2, 2.4]
for i in range(2):
    axc.add_patch(FancyArrowPatch((xs[i] + 0.26, 0), (xs[i + 1] - 0.26, 0),
                                   arrowstyle="-|>", mutation_scale=16,
                                   lw=1.8, color="#333333"))
for i, x in enumerate(xs):
    axc.add_patch(Circle((x, 0), 0.26, facecolor="#eef2f6",
                         edgecolor="#333333", lw=1.4))
    axc.text(x, 0, f"$x_{i + 1}$", ha="center", va="center", fontsize=14)
axc.set_xlim(-0.45, 2.85)
axc.set_ylim(-0.6, 0.6)
axc.set_title("(a) chain $x_1\\to x_2\\to x_3$", fontsize=11)

# --- (b) x2 not observed: x1 changes the answer ---
axb = fig.add_subplot(gs[0, 1])
vals_b = [x3_given_x1_1, x3_given_x1_0]
labs_b = ["$x_1{=}1$", "$x_1{=}0$"]
bars = axb.bar([0, 1], vals_b, width=0.5,
               color=["#d97757", "#6a9fd6"], edgecolor="#333333", lw=0.7)
for b, v in zip(bars, vals_b):
    axb.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.2f}",
             ha="center", va="bottom", fontsize=11)
axb.set_xticks([0, 1], labs_b, fontsize=11)
axb.set_ylim(0, 1.0)
axb.set_ylabel("$P(x_3{=}1\\mid\\cdot)$")
axb.set_title("(b) $x_2$ not observed: dependent", fontsize=11)
axb.grid(axis="y", alpha=0.3)

# --- (c) x2 observed: x1 no longer matters ---
axd = fig.add_subplot(gs[0, 2])
groups = ["$x_2{=}1$", "$x_2{=}0$"]
pair1 = [p31, p31]   # x1=1, x1=0
pair2 = [p30, p30]
xpos = np.array([0.0, 1.0])
w = 0.32
for off, v, col, lab in [(-w / 2 - 0.02, pair1, "#d97757", "$x_1{=}1$"),
                          (w / 2 + 0.02, pair2, "#6a9fd6", "$x_1{=}0$")]:
    axd.bar(xpos + off, v, width=w, color=col, edgecolor="#333333", lw=0.7,
            label=lab)
for x, v in zip(xpos - w / 2 - 0.02, pair1):
    axd.text(x, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=10)
for x, v in zip(xpos + w / 2 + 0.02, pair2):
    axd.text(x, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=10)
axd.set_xticks(xpos, groups, fontsize=11)
axd.set_ylim(0, 1.0)
axd.set_ylabel("$P(x_3{=}1\\mid\\cdot)$")
axd.set_title("(c) $x_2$ observed: independent of $x_1$", fontsize=11)
axd.legend(fontsize=9, loc="upper center", ncol=2, frameon=False)
axd.grid(axis="y", alpha=0.3)

fig.savefig("assets/figures/lec02-bn-conditional-independence.png", dpi=200,
            bbox_inches="tight", facecolor="white")
print("saved assets/figures/lec02-bn-conditional-independence.png")
print("p(x3=1|x1=1)=", round(x3_given_x1_1, 4),
      "p(x3=1|x1=0)=", round(x3_given_x1_0, 4))
print("given x2: 0.80 / 0.20 regardless of x1")
