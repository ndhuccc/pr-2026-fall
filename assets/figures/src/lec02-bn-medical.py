"""Figure code: lec02-bn-medical. A medical-diagnosis Bayesian network.

Root node S (smoking) leads to two diseases, C (lung cancer) and H (heart
disease). Each disease leads to two medical tests: C1, C2 for cancer and
H1, H2 for heart disease. The conditional probability tables shown are
illustrative, e.g. P(C=True | S=True) = 0.20.
All on-figure text is English / math only.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

plt.rcParams["mathtext.fontset"] = "cm"

pos = {
    "S": (2.6, 4.0),
    "C": (1.3, 2.7),
    "H": (3.9, 2.7),
    "C1": (0.5, 1.3),
    "C2": (2.1, 1.3),
    "H1": (3.1, 1.3),
    "H2": (4.7, 1.3),
}
edges = [("S", "C"), ("S", "H"),
         ("C", "C1"), ("C", "C2"),
         ("H", "H1"), ("H", "H2")]
labels = {"S": r"$S$", "C": r"$C$", "H": r"$H$",
          "C1": r"$C_1$", "C2": r"$C_2$", "H1": r"$H_1$", "H2": r"$H_2$"}
root = "S"
r = 0.32

fig, ax = plt.subplots(figsize=(7.4, 5.6))
ax.set_aspect("equal")

for a, b in edges:
    ax.add_patch(FancyArrowPatch(
        pos[a], pos[b], arrowstyle="-|>", mutation_scale=15,
        lw=1.6, color="#333333", shrinkA=22, shrinkB=24, zorder=2))

for name, (px, py) in pos.items():
    face = "#f2d6c4" if name == root else "#cfe0f2"
    ax.add_patch(Circle((px, py), r, facecolor=face,
                        edgecolor="#333333", lw=1.4, zorder=3))
    ax.text(px, py, labels[name], ha="center", va="center",
            fontsize=15, zorder=4)

ax.text(pos["S"][0], pos["S"][1] + r + 0.12, "smoking (root)",
        ha="center", va="bottom", fontsize=9.5, color="#a0522d")
ax.text(pos["C"][0], pos["C"][1] + r + 0.10, "lung cancer",
        ha="center", va="bottom", fontsize=9)
ax.text(pos["H"][0], pos["H"][1] + r + 0.10, "heart disease",
        ha="center", va="bottom", fontsize=9)
for n, lab in [("C1", "C-test 1"), ("C2", "C-test 2"),
               ("H1", "H-test 1"), ("H2", "H-test 2")]:
    ax.text(pos[n][0], pos[n][1] - r - 0.14, lab,
            ha="center", va="top", fontsize=8.5, color="#555555")

ax.text(2.6, 0.42,
        r"example CPT:  $P(C{=}\text{True}\mid S{=}\text{True})=0.20$",
        ha="center", va="center", fontsize=11, color="#333333")

ax.set_xlim(-0.1, 5.3)
ax.set_ylim(0.05, 4.75)
ax.axis("off")
fig.tight_layout()
fig.savefig("assets/figures/lec02-bn-medical.png", dpi=200,
            bbox_inches="tight", facecolor="white")
print("saved assets/figures/lec02-bn-medical.png")
