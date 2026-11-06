"""Rebuild the original diagrams for Feature Generation I / KP01.

The four observations are a deterministic teaching example, not sampled data.
Run this script from any directory; outputs stay beside the figure sources.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parents[1]
X = np.array([[1., 3.], [5., 7.], [3., 1.], [7., 5.]])
M = X.mean(axis=1)
R = X[:, 1] - X[:, 0]
COLORS = ["#176B91", "#176B91", "#BA591A", "#BA591A"]
plt.rcParams.update({"font.size": 13, "mathtext.fontset": "cm",
                     "axes.spines.top": False, "axes.spines.right": False})


def scatter(ax, values, names=True):
    for i, row in enumerate(values):
        ax.scatter(*row, s=90, c=COLORS[i], marker="o" if i < 2 else "s", zorder=4)
        if names:
            ax.annotate(f"R{i+1}", xy=row, xytext=(6, 7), textcoords="offset points", color=COLORS[i])
    ax.grid(alpha=.18)
    ax.set_aspect("equal")


def maps():
    fig = plt.figure(figsize=(10, 7.6), layout="constrained")
    grid = fig.add_gridspec(2, 2, width_ratios=[1, 1.1])
    axes = [fig.add_subplot(grid[:, 0]), fig.add_subplot(grid[0, 1]), fig.add_subplot(grid[1, 1])]
    ax = axes[0]
    scatter(ax, X)
    ax.plot([0, 8], [0, 8], "--", color="#7B8790", lw=1)
    ax.set(xlim=(0, 8), ylim=(0, 8), xlabel=r"Reading $x_1$", ylabel=r"Reading $x_2$",
           title="Original observations")
    ax = axes[1]
    for i, m in enumerate(M):
        offset = .16 if i < 2 else -.16
        ax.scatter(m, offset, s=100, color=COLORS[i], marker="o" if i < 2 else "s", zorder=4)
        ax.text(m, offset + (.13 if i < 2 else -.2), f"R{i+1}", ha="center", color=COLORS[i])
    for value in sorted(set(M)):
        ax.plot([value, value], [-.16, .16], ":", color="#A6ADB4")
    ax.axhline(0, color="#A6ADB4", lw=1)
    ax.set(xlim=(0, 8), ylim=(-.65, .65), xlabel=r"Mean $m=(x_1+x_2)/2$",
           yticks=[], title="Same mean, different classes")
    ax.spines[["left", "bottom"]].set_visible(False)
    ax.text(.5, .05, "Vertical offsets only prevent overlap", transform=ax.transAxes,
            ha="center", fontsize=10, color="#59656E")
    ax = axes[2]
    for value, color, marker, names in [(2, COLORS[0], "o", "R1, R2: class A"),
                                        (-2, COLORS[2], "s", "R3, R4: class B")]:
        ax.scatter(value, 0, s=120, color=color, marker=marker, zorder=4)
        ax.text(value, .2, names, ha="center", color=color, fontsize=11)
    ax.axhline(0, color="#A6ADB4", lw=1)
    ax.axvline(0, color="#7B8790", lw=1, ls="--")
    ax.set(xlim=(-4, 4), ylim=(-.65, .65), xlabel=r"Contrast $r=x_2-x_1$",
           yticks=[], title="The sign preserves the labels")
    ax.spines[["left", "bottom"]].set_visible(False)
    fig.savefig(OUT/'lec10-kp01-task-relevant-features.png', dpi=200, bbox_inches="tight", pad_inches=.18)
    plt.close(fig)


def reconstruction():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), layout="constrained")
    ax = axes[0]
    ax.set(xlim=(0, 5), ylim=(0, 5), xlabel=r"$x_1$", ylabel=r"$x_2$",
           title="Mean-only reconstruction loses a distinction")
    ax.set_aspect("equal")
    ax.grid(alpha=.18)
    for i in [0, 2]:
        point = X[i]
        ax.scatter(*point, s=110, color=COLORS[i], marker="o" if i == 0 else "s", zorder=5)
        ax.text(point[0] + .12, point[1] + .18, f"R{i+1}", color=COLORS[i])
        ax.annotate("", xy=(2, 2), xytext=point,
                    arrowprops={"arrowstyle":"-|>", "color":COLORS[i], "lw":2.3, "shrinkB":8})
    ax.scatter(2, 2, marker="*", s=200, color="#5F6A72", zorder=6)
    ax.text(2.25, 2.45, r"$(m,m)=(2,2)$", color="#46535D")
    ax.text(.5, .07, r"Squared error $1^2+1^2=2$ for each row",
            transform=ax.transAxes, ha="center", fontsize=11)
    ax = axes[1]
    scatter(ax, np.column_stack((M, R)))
    ax.set(xlim=(0, 8), ylim=(-4, 4), xlabel=r"Mean $m$", ylabel=r"Contrast $r$",
           title="Keep both features: the map is reversible")
    ax.axhline(0, color="#9EA8B0", lw=1)
    ax.text(.5, .02, r"$x_1=m-r/2$     $x_2=m+r/2$", transform=ax.transAxes,
            ha="center", fontsize=14)
    fig.savefig(OUT/'lec10-kp01-reconstruction.png', dpi=200, bbox_inches="tight", pad_inches=.18)
    plt.close(fig)


def protocol():
    fig, ax = plt.subplots(figsize=(12, 4.8), layout="constrained")
    ax.set(xlim=(0, 12), ylim=(0, 4.8))
    ax.axis("off")
    nodes = {"train":(1.8,3.5,"Training observations\nand available labels"),
             "fit":(5.8,3.5,"Fit the transformation\nTransform training data"),
             "model":(10,3.5,"Train the model\non training features"),
             "test":(1.8,1,"Held-out observations\nKeep them separate"),
             "apply":(5.8,1,"Apply the SAME\nfixed transformation"),
             "eval":(10,1,"Predict with fixed model\nEvaluate the chosen task")}
    for key, (cx,cy,label) in nodes.items():
        face = "#E9F2F6" if key in ("train","fit","model") else "#FFF1E7"
        ax.add_patch(FancyBboxPatch((cx-1.55,cy-.5),3.1,1,boxstyle="round,pad=.10",
                                   facecolor=face,edgecolor="#55707F",lw=1.5))
        ax.text(cx,cy,label,ha="center",va="center",fontsize=14)
    for start,end in [((3.45,3.5),(4.15,3.5)),((7.45,3.5),(8.35,3.5)),
                      ((3.45,1),(4.15,1)),((7.45,1),(8.35,1)),
                      ((5.8,2.9),(5.8,1.6)),((10,2.9),(10,1.6))]:
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=18,
                                    color="#526D7B",lw=1.8))
    ax.text(5.6,2.25,"learned settings",ha="right",fontsize=10,color="#526D7B")
    ax.text(9.8,2.25,"fixed model",ha="right",fontsize=10,color="#526D7B")
    ax.text(6,4.55,"Separate data before learning the representation",ha="center",fontsize=17)
    fig.savefig(OUT/'lec10-kp01-training-protocol.png', dpi=200, bbox_inches="tight", pad_inches=.18)
    plt.close(fig)


if __name__ == '__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    maps()
    reconstruction()
    protocol()
    print('Rebuilt 3 diagrams from the four stated observations and the declared information flow.')
