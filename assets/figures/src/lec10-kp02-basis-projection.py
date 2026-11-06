"""Rebuild the three measured diagrams for Lecture 10, KP02.

Run from any directory. All coordinates and image cells come from the worked
examples; no random data or manually traced curves are used.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

OUT = Path(__file__).resolve().parents[1]
plt.rcParams.update({"font.size": 12, "mathtext.fontset": "cm", "axes.spines.top": False,
                     "axes.spines.right": False, "savefig.facecolor": "white"})
A = np.array([[3 / 5, -4 / 5], [4 / 5, 3 / 5]])
x = np.array([2., 11.])
y = A.T @ x
p = A[:, 0] * y[0]
r = A[:, 1] * y[1]
BLUE, ORANGE, PURPLE = "#176B91", "#B65A13", "#7951A3"


def arrow(ax, start, end, color, lw=2.5):
    ax.annotate("", xy=end, xytext=start,
                arrowprops={"arrowstyle": "-|>", "color": color, "lw": lw,
                            "mutation_scale": 18}, zorder=4)


def plane(ax):
    ax.set_aspect("equal")
    ax.set(xlim=(-6, 10), ylim=(-2, 14), xlabel=r"$x_1$", ylabel=r"$x_2$")
    ax.axhline(0, color="#AAB4BC", lw=.8)
    ax.axvline(0, color="#AAB4BC", lw=.8)
    ax.grid(alpha=.15)


def coordinate_figure():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), layout="constrained")
    ax = axes[0]
    plane(ax)
    ax.set_title("One vector, two perpendicular components", pad=16)
    ax.add_patch(Polygon([[0, 0], p, x, r], closed=True, color=BLUE, alpha=.08))
    ax.plot([0, r[0]], [0, r[1]], "--", color=PURPLE, alpha=.6)
    ax.plot([r[0], x[0]], [r[1], x[1]], "--", color=ORANGE, alpha=.6)
    arrow(ax, [0, 0], p, ORANGE)
    arrow(ax, p, x, PURPLE)
    ax.scatter(*x, s=65, color=BLUE, zorder=6)
    ax.text(2.5, 11.6, r"$\mathbf{x}=(2,11)^T$", color=BLUE)
    ax.text(7.3, 5.4, r"$10\mathbf{a}_1$" + "\n" + r"$(6,8)^T$", color=ORANGE, ha="center")
    ax.text(-3.3, 8.3, r"$5\mathbf{a}_2$" + "\n" + r"$(-4,3)^T$", color=PURPLE, ha="center")
    # The marker is constructed in the orthonormal basis, so it is a true right angle.
    corner = np.array([p - .6 * A[:, 0], p - .6 * A[:, 0] + .6 * A[:, 1],
                       p + .6 * A[:, 1]])
    ax.plot(corner[:, 0], corner[:, 1], color="#57636C", lw=1.4)
    ax = axes[1]
    ax.set_aspect("equal")
    ax.set(xlim=(-1, 13), ylim=(-1, 13), xlabel=r"$y_1$ along $\mathbf{a}_1$",
           ylabel=r"$y_2$ along $\mathbf{a}_2$")
    ax.set_title("Coordinates in the new basis", pad=16)
    ax.axhline(0, color="#AAB4BC", lw=.8)
    ax.axvline(0, color="#AAB4BC", lw=.8)
    ax.grid(alpha=.15)
    ax.fill([0, y[0], y[0], 0], [0, 0, y[1], y[1]], color=BLUE, alpha=.08)
    arrow(ax, [0, 0], y, BLUE)
    ax.plot([y[0], y[0]], [0, y[1]], "--", color=PURPLE)
    ax.plot([0, y[0]], [y[1], y[1]], "--", color=ORANGE)
    ax.scatter(*y, s=65, color=BLUE, zorder=6)
    ax.text(8.4, 6.1, r"$\mathbf{y}=(10,5)^T$", color=BLUE)
    ax.text(5, -.7, r"$y_1=10$", color=ORANGE, ha="center")
    ax.text(.5, 5.5, r"$y_2=5$", color=PURPLE)
    fig.savefig(OUT / "lec10-kp02-coordinate-change.png", dpi=200, bbox_inches="tight", pad_inches=.18)
    plt.close(fig)


def truncation_figure():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), layout="constrained")
    ax = axes[0]
    plane(ax)
    ax.set_title("Discard the second coordinate: error length = 5", pad=16)
    t = np.array([-3., 16.])
    ax.plot(t * A[0, 0], t * A[1, 0], color=ORANGE, alpha=.5, lw=2)
    arrow(ax, [0, 0], p, ORANGE)
    arrow(ax, p, x, PURPLE)
    ax.scatter(*x, color=BLUE, s=70, zorder=6)
    ax.scatter(*p, color=ORANGE, s=70, zorder=6)
    ax.text(-.5, 12, r"$\mathbf{x}=(2,11)^T$", color=BLUE)
    ax.text(5.6, 7.1, r"$\hat{\mathbf{x}}=(6,8)^T$", color=ORANGE, ha="center")
    ax.text(-3.5, 7.6, r"$\mathbf{e}=(-4,3)^T$" + "\n" + r"$\|\mathbf{e}\|=5$", color=PURPLE)
    corner = np.array([p - .6 * A[:, 0], p - .6 * A[:, 0] + .6 * A[:, 1],
                       p + .6 * A[:, 1]])
    ax.plot(corner[:, 0], corner[:, 1], color="#57636C", lw=1.4)
    ax = axes[1]
    energies = [float(x @ x), float(y[0] ** 2), float(y[1] ** 2)]
    bars = ax.bar([0, 1, 2], energies, width=.6, color=[BLUE, ORANGE, PURPLE])
    ax.set(xticks=[0, 1, 2], xticklabels=["Original", "Retained", "Discarded"],
           ylabel="Squared length", ylim=(0, 155), title="125 = 100 + 25")
    ax.grid(axis="y", alpha=.15)
    ax.set_axisbelow(True)
    for bar, value in zip(bars, energies):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 4, f"{value:g}", ha="center")
    ax.text(.5, .91, r"$\|\mathbf{x}-\hat{\mathbf{x}}\|^2=y_2^2=25$",
            transform=ax.transAxes, ha="center", fontsize=16)
    fig.savefig(OUT / "lec10-kp02-truncation-error.png", dpi=200, bbox_inches="tight", pad_inches=.18)
    plt.close(fig)


def image_figure():
    H = np.array([[1., 1.], [1., -1.]]) / np.sqrt(2)
    X = np.array([[4., 2.], [1., 3.]])
    Y = H.T @ X @ H
    bases = [np.outer(H[:, i], H[:, j]) for i in range(2) for j in range(2)]
    weights = np.array([5., 0., 1., 2.])
    assert np.allclose(Y.ravel(), weights)
    reconstructed = sum(w * b for w, b in zip(weights, bases))
    assert np.allclose(reconstructed, X)
    fig, axes = plt.subplots(2, 5, figsize=(14, 6), layout="constrained")
    for k, (base, w) in enumerate(zip(bases, weights)):
        i, j = divmod(k, 2)
        for row, data, vmax in [(0, base, .5), (1, w * base, 3.5)]:
            ax = axes[row, k]
            ax.imshow(data, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
            ax.set(xticks=[], yticks=[])
            ax.set_title((r"$B_{%d%d}$" if row == 0 else r"$%g B_{%d%d}$") %
                         ((i + 1, j + 1) if row == 0 else (w, i + 1, j + 1)))
            for rr in range(2):
                for cc in range(2):
                    v = float(data[rr, cc])
                    if abs(v) < 1e-12:
                        v = 0.0
                    ax.text(cc, rr, f"{v:.1f}", ha="center", va="center", fontsize=16,
                            color="white" if abs(v) > .65 * vmax else "#172B3A")
    for row, (data, title) in enumerate([(X, r"Original $X$"), (reconstructed, r"$\sum_{ij}Y_{ij}B_{ij}$")]):
        ax = axes[row, 4]
        ax.imshow(data, cmap="Greys_r", vmin=0, vmax=4)
        ax.set(xticks=[], yticks=[], title=title)
        for rr in range(2):
            for cc in range(2):
                ax.text(cc, rr, f"{data[rr,cc]:g}", ha="center", va="center", fontsize=17,
                        color="#172B3A" if data[rr,cc] >= 2 else "white")
    fig.suptitle("Basis images (top) and weighted contributions (bottom)", fontsize=18)
    fig.savefig(OUT / "lec10-kp02-basis-images.png", dpi=200, bbox_inches="tight", pad_inches=.18)
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    coordinate_figure()
    truncation_figure()
    image_figure()
    print("Rebuilt 3 figures from the stated vectors and matrices.")
